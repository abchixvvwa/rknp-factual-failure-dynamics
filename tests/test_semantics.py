import pytest

from src.semantics.clustering import validate_groups, deterministic_groups
from src.semantics.validate_judge import agreement


def test_groups_and_no_false_lexical_merges():
    assert deterministic_groups(["1", "1.0", "2"]) == [[0, 1], [2]]
    assert deterministic_groups(["Mercury has moons", "Mercury has no moons"]) is None
    assert deterministic_groups(["Lake Baikal", "Baikal"]) is None
    assert validate_groups({"groups": [{"group_id": 9, "members": ["B", "A"]}], "uncertain": False}, 2) == ([[0, 1]], False)


@pytest.mark.parametrize("members", [["A", "A"], ["A"], ["A", "Z"]])
def test_bad_partition_rejected(members):
    with pytest.raises(ValueError):
        validate_groups({"groups": [{"group_id": 0, "members": members}], "uncertain": False}, 2)


def test_permutation_invariant_judge_validation():
    result = agreement([0, 0, 1, 2], [8, 8, 3, 4])
    assert result == dict(adjusted_rand_index=1.0, pairwise_agreement=1.0, exact_cluster_match=True)


def test_judge_schema_prefix_blinding_and_cache(tmp_path, config):
    import json
    from src.generation.store import Store
    from src.semantics.judge import group_answers
    class Judge:
        calls = 0
        def complete(self, payload):
            self.calls += 1
            text = payload["messages"][0]["content"]
            assert "SECRET_GROUND_TRUTH" not in text and "FUTURE_SAMPLE" not in text
            schema = payload["response_format"]["json_schema"]
            assert schema["strict"] is True
            assert schema["schema"]["properties"]["assignments"]["required"] == ["A", "B"]
            response = dict(choices=[dict(message=dict(content=json.dumps({"assignments": {"A": 0, "B": 1}, "uncertain": False})),
                                         finish_reason="stop")], usage=dict(prompt_tokens=100, completion_tokens=20, total_tokens=120))
            return response, {}, 200
    case = dict(case_id="fixture", language="en", question="Fixture question?", canonical="SECRET_GROUND_TRUTH",
                samples=["Alpha", "Beta", "FUTURE_SAMPLE"])
    store, client = Store(tmp_path / "ledger.db"), Judge()
    for _ in range(2):
        groups, uncertain, audit = group_answers(store, client, config, "test", case, ["Alpha", "Beta"], tmp_path / "log")
        assert groups == [[0], [1]] and not uncertain
    assert client.calls == 1
    store.close()


def test_judge_truncation_recovery_keeps_original(tmp_path, config):
    import json
    from src.generation.store import Store
    from src.semantics.judge import group_answers
    class Judge:
        calls = []
        def complete(self, payload):
            cap = payload["max_completion_tokens"]
            self.calls.append(cap)
            text = "{" if cap == 256 else json.dumps({"assignments": {"A": 0, "B": 1}, "uncertain": False})
            return dict(choices=[dict(message=dict(content=text), finish_reason="length" if cap == 256 else "stop")],
                        usage=dict(prompt_tokens=50, completion_tokens=cap, total_tokens=50+cap)), {}, 200
    store, client = Store(tmp_path / "ledger.db"), Judge()
    case = dict(case_id="fixture", language="en", question="Fixture?")
    groups, uncertain, audit = group_answers(store, client, config, "unit", case, ["Alpha", "Beta"], tmp_path / "log")
    assert client.calls == [256, 1024]
    assert audit["truncated_request_id"] and audit["effective_max_completion_tokens"] == 1024
    group_answers(store, client, config, "unit", case, ["Alpha", "Beta"], tmp_path / "log")
    assert client.calls == [256, 1024]
    assert store.db.execute("SELECT COUNT(*) FROM attempts").fetchone()[0] == 2
    store.close()


def test_joint_judge_returns_all_prefixes_in_one_request(tmp_path, config):
    import json
    from src.generation.store import Store
    from src.semantics.judge import judge_case_joint, JUDGE_VERSION

    class Judge:
        calls = 0

        def complete(self, payload):
            self.calls += 1
            prompt = payload["messages"][0]["content"]
            assert "SECRET_GROUND_TRUTH" not in prompt
            assert all(f'"{letter}"' in prompt for letter in "ABCDE")
            response = {
                "labels": [[1 if letter in "AC" else 0 for letter in "ABCDE"] for _ in range(4)],
                "target_labels": [1, 1, 1, 1],
                "uncertain": [False, False, False, False],
            }
            return dict(choices=[dict(message=dict(content=json.dumps(response)), finish_reason="stop")],
                        usage=dict(prompt_tokens=200, completion_tokens=100, total_tokens=300)), {}, 200

    case = dict(case_id="joint", language="en", question="Fixture?", canonical="SECRET_GROUND_TRUTH",
                target={"response_text": "Alpha"},
                samples=[{"response_text": value} for value in ["Alpha", "Beta", "Alpha", "Gamma", "Delta"]])
    store, client = Store(tmp_path / "ledger.db"), Judge()
    prefixes = judge_case_joint(store, client, config, "unit", case, tmp_path / "log")
    assert client.calls == 1
    assert [prefix["k"] for prefix in prefixes] == [2, 3, 4, 5]
    assert prefixes[0]["groups"] == [[0], [1]] and prefixes[0]["target_group"] == 0
    assert prefixes[-1]["groups"] == [[0, 2], [1, 3, 4]] and prefixes[-1]["target_group"] == 0
    assert all(prefix["audit"]["judge_prompt_version"] == JUDGE_VERSION for prefix in prefixes)
    store.close()


def test_joint_judge_skips_api_when_every_prefix_is_deterministic(tmp_path, config):
    from src.generation.store import Store
    from src.semantics.judge import judge_case_joint

    class Judge:
        def complete(self, payload):
            raise AssertionError("deterministic case must not call the API")

    case = dict(case_id="exact", language="en", question="Fixture?",
                target={"response_text": "42"},
                samples=[{"response_text": value} for value in ["42", "42.0", "42", "42", "42"]])
    store = Store(tmp_path / "ledger.db")
    prefixes = judge_case_joint(store, Judge(), config, "unit", case, tmp_path / "log")
    assert [prefix["target_group"] for prefix in prefixes] == [0, 0, 0, 0]
    assert all(prefix["audit"] is None for prefix in prefixes)
    store.close()

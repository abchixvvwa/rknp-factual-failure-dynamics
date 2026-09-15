import pytest

from src.benchmark.validate import read_benchmark


def test_valid_fixture(fact_row, write_facts):
    assert read_benchmark(write_facts([fact_row]))[0].fact_id == "fixture_1"


@pytest.mark.parametrize("field,value", [
    ("source_url", ""), ("source_url", "file:///tmp/source"), ("question_kk", " "),
    ("question_ru", ""), ("canonical_answer", ""), ("acceptable_aliases_json", "{}"),
    ("acceptable_aliases_json", '[12]'), ("category", "unknown"),
    ("false_premise", True), ("source_accessed_date", "2999-01-01"),
])
def test_bad_rows_fail(fact_row, write_facts, field, value):
    with pytest.raises(ValueError):
        read_benchmark(write_facts([dict(fact_row, **{field: value})]))


def test_duplicate_and_unverified_main_fail(fact_row, write_facts):
    with pytest.raises(ValueError, match="Duplicate fact_id"):
        read_benchmark(write_facts([fact_row, fact_row]))
    with pytest.raises(ValueError, match="human-verified"):
        read_benchmark(write_facts([fact_row]), main=True)
    assert read_benchmark(write_facts([dict(fact_row, verified_by_human=True)]), main=True)


def test_empty_benchmark_rejected(write_facts):
    with pytest.raises(ValueError, match="empty"):
        read_benchmark(write_facts([]))


def test_scientific_pilot_review_gate_precedes_any_api_call(config, fact_row, write_facts, monkeypatch):
    from types import SimpleNamespace
    import src.generation.run as generation
    config["paths"]["benchmark"] = str(write_facts([fact_row]))
    config["pilot"]["require_human_verified"] = True
    args = SimpleNamespace(dry_run=False, limit=None, model=None, language=None, experiment_id="unit", retry_uncertain=False)
    monkeypatch.setattr(generation, "run_specs", lambda *a, **kw: pytest.fail("No API stage may run before review"))
    with pytest.raises(ValueError, match="awaits human verification"):
        generation.pilot(args, config)
    args.dry_run = True
    assert generation.pilot(args, config)["pending_human_verification"] == 1

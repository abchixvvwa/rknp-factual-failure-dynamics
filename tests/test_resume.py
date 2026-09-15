import json

import pandas as pd
import pytest

from src.generation.store import Store
from src.generation.scheduler import execute
from src.groq.client import RequestFailed


class FakeClient:
    def __init__(self, fail=None, finish="stop", content="Fixture"):
        self.calls, self.fail, self.finish, self.content = 0, fail, finish, content

    def complete(self, payload):
        self.calls += 1
        assert payload["n"] == 1 and "logprobs" not in payload
        if self.fail and self.calls == 1:
            raise self.fail
        return (dict(id="fake_unit_test", choices=[dict(message=dict(content=self.content), finish_reason=self.finish)],
                     usage=dict(prompt_tokens=10, completion_tokens=3, total_tokens=13), system_fingerprint="unit_test"), {}, 200)


def test_restart_deduplicates_and_exports(tmp_path, spec, config):
    path = tmp_path / "ledger.db"
    store = Store(path)
    client = FakeClient()
    with store.writer_lock():
        record, created = execute(store, client, spec, config["groq"], tmp_path / "log")
    assert created and record["system_fingerprint"] == "unit_test"
    assert json.loads(record["raw_response_json"])["id"] == "fake_unit_test"
    store.close()
    store = Store(path)
    record2, created = execute(store, client, spec, config["groq"], tmp_path / "log")
    assert not created and record2 == record and client.calls == 1
    store.export(tmp_path / "generations.parquet")
    assert len(pd.read_parquet(tmp_path / "generations.parquet")) == 1
    with pytest.raises(ValueError, match="different prompt"):
        store.register(dict(spec, prompt_text="Changed"))
    store.close()


def test_retry_persists_failure_not_duplicate_success(tmp_path, spec, config, monkeypatch):
    store = Store(tmp_path / "ledger.db")
    monkeypatch.setattr("src.generation.scheduler.retry_delay", lambda *args: 0)
    client = FakeClient(RequestFailed(429, "RateLimit", "test"))
    execute(store, client, spec, config["groq"], tmp_path / "log")
    assert client.calls == 2
    assert dict(store.db.execute("SELECT state,count(*) FROM attempts GROUP BY state").fetchall()) == dict(failed=1, success=1)
    assert store.db.execute("SELECT retry FROM attempts WHERE state='success'").fetchone()[0] == 1
    store.close()


def test_structured_json_validation_400_is_retried(tmp_path, spec, config, monkeypatch):
    store = Store(tmp_path / "ledger.db")
    monkeypatch.setattr("src.generation.scheduler.retry_delay", lambda *args: 0)
    client = FakeClient(RequestFailed(400, "BadRequestError", "json_validate_failed"))
    record, created = execute(store, client, spec, config["groq"], tmp_path / "log")
    assert created and record["valid_response"] and client.calls == 2
    assert [(r[0], r[1]) for r in store.db.execute("SELECT status,state FROM attempts ORDER BY id")] == [(400, "failed"), (200, "success")]
    store.close()


@pytest.mark.parametrize("status", [400, 401, 403])
def test_fatal_http_errors_stop(tmp_path, spec, config, status):
    store = Store(tmp_path / "ledger.db")
    client = FakeClient(RequestFailed(status, "Fatal", "test"))
    with pytest.raises(RequestFailed):
        execute(store, client, spec, config["groq"], tmp_path / "log")
    assert client.calls == 1
    if status == 400:
        with pytest.raises(RuntimeError, match="previously failed"):
            execute(store, client, spec, config["groq"], tmp_path / "log")
        assert client.calls == 1
    store.close()


def test_crash_requires_explicit_retry(tmp_path, spec, config):
    from src.groq.budget import Budget
    store = Store(tmp_path / "ledger.db")
    key = store.register(spec)
    Budget(store, config["groq"]).reserve(key, "test_model", 10, 96, 0)
    store.close()
    store = Store(tmp_path / "ledger.db")
    with pytest.raises(RuntimeError, match="in-flight"):
        execute(store, FakeClient(), spec, config["groq"], tmp_path / "log")
    execute(store, FakeClient(), spec, config["groq"], tmp_path / "log", retry_uncertain=True)
    assert store.db.execute("SELECT COUNT(*) FROM attempts WHERE state='uncertain'").fetchone()[0] == 1
    store.close()


@pytest.mark.parametrize("finish,content", [("length", "partial"), ("stop", ""), ("content_filter", "refusal")])
def test_invalid_responses_preserved_but_not_usable(tmp_path, spec, config, finish, content):
    store = Store(tmp_path / "ledger.db")
    record, _ = execute(store, FakeClient(finish=finish, content=content), spec, config["groq"], tmp_path / "log")
    assert not record["valid_response"]
    assert record["response_text"] == content
    store.close()


def test_immutable_experiment(tmp_path):
    store = Store(tmp_path / "ledger.db")
    store.register_experiment("test", {"seed": 42}, {})
    store.register_experiment("test", {"seed": 42}, {})
    with pytest.raises(ValueError, match="inputs changed"):
        store.register_experiment("test", {"seed": 43}, {})
    store.close()

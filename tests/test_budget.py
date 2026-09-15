import pytest

from src.generation.store import Store
from src.groq.budget import Budget, BudgetExhausted, ResumeLater
from src.groq.limiter import apply_headers
from src.groq.retry import retry_delay, duration, retryable


def test_budget_survives_restart_and_resets_at_utc_day(tmp_path, spec, config):
    config["groq"]["enforce_local_limits"] = True
    path = tmp_path / "ledger.db"
    config["groq"]["daily_request_cap"] = 1
    store = Store(path)
    key = store.register(spec)
    Budget(store, config["groq"]).reserve(key, "test_model", 10, 96, 0, now=86400)
    store.close()
    store = Store(path)
    budget = Budget(store, config["groq"])
    with pytest.raises(BudgetExhausted):
        budget.reserve(key, "test_model", 10, 96, 0, now=86500)
    budget.reserve(key, "test_model", 10, 96, 0, now=172800)
    assert budget.summary(now=172800)["requests_today"] == 1
    assert budget.summary(now=172800)["per_model"][0]["actual_input_tokens"] is None
    store.close()


def test_rpm_and_tokens(tmp_path, spec, config):
    config["groq"]["enforce_local_limits"] = True
    store = Store(tmp_path / "ledger.db")
    key = store.register(spec)
    config["groq"]["limits"]["requests_per_minute"] = 1
    budget = Budget(store, config["groq"])
    budget.reserve(key, "test_model", 10, 96, 0, now=1000)
    with pytest.raises(ResumeLater):
        budget.reserve(key, "test_model", 10, 96, 1, now=1001)
    with pytest.raises(BudgetExhausted, match="TPM"):
        budget.reserve(key, "other_model", 10000, 96, 0, now=1001)
    budget.reserve(key, "test_model", 10, 96, 1, now=1061)
    store.close()


def test_backoff_and_response_headers(tmp_path):
    assert duration("2m59.56s") == pytest.approx(179.56)
    assert duration("7.66s") == 7.66
    assert duration("bad") is None
    assert retry_delay(0, {"retry-after": "3600"}, cap=60) == 3600
    assert retryable(500) and retryable(429) and retryable(None)
    assert not retryable(400) and not retryable(403)
    store = Store(tmp_path / "ledger.db")
    apply_headers(store, "test_model", {"x-ratelimit-remaining-requests": "0", "x-ratelimit-reset-requests": "1h"})
    assert store.db.execute("SELECT until FROM cooldowns").fetchone() is not None
    store.close()


def test_provider_only_preserves_cooldowns_and_ledger(tmp_path, spec, config):
    config["groq"]["enforce_local_limits"] = False
    config["groq"]["daily_request_cap"] = 1
    config["groq"]["limits"] = dict.fromkeys(config["groq"]["limits"], 1)
    store = Store(tmp_path / "ledger.db")
    key = store.register(spec)
    budget = Budget(store, config["groq"])
    budget.reserve(key, "test_model", 10000, 512, 0, now=1000)
    budget.reserve(key, "test_model", 10000, 512, 1, now=1001)
    assert budget.summary(now=1001)["requests_today"] == 2
    apply_headers(store, "test_model", {"retry-after": "120"}, status=429)
    with pytest.raises(ResumeLater):
        budget.reserve(key, "test_model", 10000, 512, 2)
    store.close()

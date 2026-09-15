import pytest

from src.groq.client import Client
from src.groq.models import require_models
from src.utils.logging import event


def test_no_key_no_network(config, monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="missing"):
        Client(config["groq"])


def test_only_groq_endpoint(config):
    config["groq"]["base_url"] = "https://example.org"
    with pytest.raises(ValueError, match="Non-Groq"):
        Client(config["groq"])


def test_log_redaction(tmp_path, monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "unit_secret_key")
    path = tmp_path / "log"
    event(path, "test", details="unit_secret_key")
    assert "unit_secret_key" not in path.read_text()


def test_model_substitution_forbidden():
    with pytest.raises(RuntimeError, match="unavailable"):
        require_models({"data": [{"id": "available", "active": True}]}, ["missing"])


def test_sdk_endpoint_is_not_duplicated(config, monkeypatch):
    import httpx
    import groq
    monkeypatch.setenv("GROQ_API_KEY", "unit_secret")
    visited = []
    def transport(request):
        visited.append(str(request.url))
        return httpx.Response(200, json={"object": "list", "data": []})
    def sdk(**kwargs):
        return groq.Groq(**kwargs, http_client=httpx.Client(transport=httpx.MockTransport(transport)))
    monkeypatch.setattr("src.groq.client.Groq", sdk)
    client = Client(config["groq"])
    assert client.models()["data"] == []
    client.close()
    assert visited == ["https://api.groq.com/openai/v1/models"]

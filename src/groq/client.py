import os

from groq import APIConnectionError, APIStatusError, APITimeoutError, Groq

from src.utils.logging import redact


class RequestFailed(Exception):
    def __init__(self, status, error_type, message, headers=None):
        self.status, self.error_type = status, error_type
        self.message = redact(message)
        self.headers = dict(headers or {})
        super().__init__(f"{error_type} (HTTP {status})")


class Client:
    def __init__(self, config):
        if config["base_url"] != "https://api.groq.com/openai/v1":
            raise ValueError("Non-Groq endpoints are forbidden")
        key = os.environ.get("GROQ_API_KEY", "").strip()
        if not key:
            raise RuntimeError("GROQ_API_KEY is missing; set it in the environment, never in a committed file")
        self.config = config
        # Groq SDK 1.7 includes /openai/v1 in each resource path.
        self.sdk = Groq(api_key=key, base_url="https://api.groq.com", max_retries=0,
                        timeout=config["timeout_seconds"])

    def models(self):
        try:
            raw = self.sdk.models.with_raw_response.list()
            return raw.parse().model_dump(mode="json")
        except APIStatusError as exc:
            raise RequestFailed(exc.status_code, type(exc).__name__, "Model listing rejected") from None
        except APIConnectionError:
            raise RequestFailed(None, "ConnectionError", "Cannot connect to Groq") from None

    def complete(self, payload):
        if self.config.get("free_plan_confirmed") is not True:
            raise RuntimeError("Confirm the organization is on Groq Free Plan before inference")
        if payload.get("n") != 1 or "logprobs" in payload or "top_logprobs" in payload:
            raise ValueError("Protocol requires n=1 and no logprobs")
        try:
            response = self.sdk.chat.completions.with_raw_response.create(**payload)
            return response.parse().model_dump(mode="json"), dict(response.headers), response.status_code
        except APIStatusError as exc:
            raise RequestFailed(exc.status_code, type(exc).__name__, redact(str(exc.body)), exc.response.headers) from None
        except (APITimeoutError, APIConnectionError) as exc:
            raise RequestFailed(None, type(exc).__name__, "Network failure; server execution may be unknown") from None

    def close(self):
        self.sdk.close()

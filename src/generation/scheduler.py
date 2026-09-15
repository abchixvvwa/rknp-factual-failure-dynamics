import json
import time
import uuid

from src.groq.budget import Budget, ResumeLater
from src.groq.client import RequestFailed
from src.groq.limiter import apply_headers
from src.groq.retry import retry_delay, retryable
from src.utils.hashing import text_hash
from src.utils.logging import event, redact
from src.utils.time import utc_now


def estimate_input(payload):
    # UTF-8 byte count plus overhead is intentionally conservative for EN/RU/KK.
    return len(json.dumps(payload["messages"], ensure_ascii=False).encode("utf-8")) + 128


def execute(store, client, spec, config, log_path, retry_uncertain=False):
    key = store.register(spec)
    saved = store.success(key)
    if saved:
        return saved, False
    if retry_uncertain:
        store.release_uncertain(key)
        event(log_path, "retry_uncertain_authorized", request_id=key)
    else:
        store.check_uncertain(key)
    payload = dict(model=spec["model_id"], messages=[dict(role="user", content=spec["prompt_text"])],
                   n=1, **spec["parameters"])
    budget = Budget(store, config)
    last = store.db.execute("SELECT status,record FROM attempts WHERE request_key=? ORDER BY id DESC LIMIT 1", (key,)).fetchone()
    last_message = (json.loads(last[1]).get("error_message", "") if last and last[1] else "")
    if last and last[0] == 400 and not retryable(last[0], last_message):
        raise RuntimeError("This exact request previously failed with HTTP 400. Correct/version the request instead of retrying it blindly")
    previous = store.db.execute("SELECT MAX(retry) FROM attempts WHERE request_key=?", (key,)).fetchone()[0]
    first_retry = 0 if previous is None else previous + 1
    # A later invocation is a new recovery cycle for transient transport/rate failures.
    # Keep every failed attempt in the journal, but do not permanently brick a request
    # merely because the network was unavailable for one complete retry cycle.
    if (first_retry > config["max_retries"] and last
            and retryable(last[0], last_message)):
        first_retry = 0
    for retry in range(first_retry, config["max_retries"] + 1):
        while True:
            try:
                attempt = budget.reserve(key, spec["model_id"], estimate_input(payload),
                                         payload["max_completion_tokens"], retry)
                break
            except ResumeLater as exc:
                if exc.seconds > 60:
                    raise
                time.sleep(exc.seconds)
        started = time.monotonic()
        base = {k: v for k, v in spec.items() if k != "parameters"}
        base.update(spec["parameters"])
        base.update(request_id=key, run_id=str(uuid.uuid4()), top_p=payload.get("top_p", 1.0),
                    created_at_utc=utc_now(), retry_count=retry)
        try:
            response, headers, status = client.complete(payload)
        except RequestFailed as exc:
            base.update(error_type=exc.error_type, error_message=exc.message, http_status=exc.status,
                        latency_ms=round(1000 * (time.monotonic()-started), 2))
            store.finish(attempt, "failed", base, exc.status)
            apply_headers(store, spec["model_id"], exc.headers, exc.status)
            event(log_path, "groq_request_failed", request_id=key, model_id=spec["model_id"],
                  error_type=exc.error_type, http_status=exc.status, retry_count=retry)
            if not retryable(exc.status, exc.message) or retry == config["max_retries"]:
                raise
            delay = retry_delay(retry, exc.headers, config["backoff_base_seconds"], config["backoff_cap_seconds"])
            store.defer(spec["model_id"], delay)
            if delay > 60:
                raise ResumeLater(delay) from None
            continue
        usage = response.get("usage") or {}
        choices = response.get("choices") or []
        choice = choices[0] if choices else {}
        content = (choice.get("message") or {}).get("content") or ""
        if not isinstance(content, str):
            content = ""
        finish = choice.get("finish_reason")
        base.update(response_text=content, response_sha256=text_hash(content),
                    system_fingerprint=response.get("system_fingerprint"), finish_reason=finish,
                    prompt_tokens=usage.get("prompt_tokens"), completion_tokens=usage.get("completion_tokens"),
                    total_tokens=usage.get("total_tokens"), http_status=status, error_type=None, error_message=None,
                    latency_ms=round(1000 * (time.monotonic()-started), 2),
                    api_response_id=response.get("id"), raw_response_json=redact(json.dumps(response, ensure_ascii=False)),
                    response_headers_json=json.dumps({k: v for k, v in headers.items()
                        if k.lower().startswith("x-ratelimit") or k.lower() in ("retry-after", "x-request-id")}),
                    valid_response=bool(content.strip()) and finish == "stop")
        # Preserve even empty/truncated HTTP-successful responses; never call them complete cases.
        store.finish(attempt, "success", base, status, usage)
        apply_headers(store, spec["model_id"], headers)
        event(log_path, "groq_request_success", request_id=key, model_id=spec["model_id"],
              valid_response=base["valid_response"], retry_count=retry)
        return base, True
    raise RuntimeError("Persisted retry limit exhausted for this request; inspect failures before a new run")

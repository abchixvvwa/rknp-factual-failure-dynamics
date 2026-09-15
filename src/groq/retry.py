import random
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime


def duration(value):
    if value is None:
        return None
    try:
        return max(0, float(value))
    except ValueError:
        pass
    if re.fullmatch(r"(?:\d+(?:\.\d+)?(?:ms|s|m|h))+", value):
        scales = {"ms": .001, "s": 1, "m": 60, "h": 3600}
        return sum(float(n) * scales[u] for n, u in re.findall(r"(\d+(?:\.\d+)?)(ms|s|m|h)", value))
    try:
        return max(0, (parsedate_to_datetime(value) - datetime.now(timezone.utc)).total_seconds())
    except (ValueError, TypeError, OverflowError):
        return None


def retry_delay(retry, headers, base=2, cap=60):
    backoff = random.uniform(0.5, 1.0) * min(cap, base * 2 ** retry)
    # Server Retry-After must never be shortened by the local backoff cap.
    return max(backoff, duration(headers.get("retry-after")) or 0)


def retryable(status, message=""):
    return (status is None or status == 429 or 500 <= status <= 599 or
            status == 400 and "json_validate_failed" in message)

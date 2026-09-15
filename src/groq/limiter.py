from src.groq.retry import duration


def apply_headers(store, model, headers, status=200):
    """Groq request headers describe RPD, while token headers describe TPM."""
    headers = {k.lower(): v for k, v in headers.items()}
    delays = []
    for unit in ("requests", "tokens"):
        remaining = headers.get(f"x-ratelimit-remaining-{unit}")
        try:
            exhausted = remaining is not None and float(remaining) <= 0
        except ValueError:
            exhausted = False
        if exhausted:
            # Missing reset must not cause a rapid retry on an exhausted quota.
            delays.append(duration(headers.get(f"x-ratelimit-reset-{unit}")) or (86400 if unit == "requests" else 60))
    if status == 429:
        delays.append(duration(headers.get("retry-after")) or 0)
    if delays:
        store.defer(model, max(delays))

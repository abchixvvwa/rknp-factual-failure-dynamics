import time
from datetime import datetime, timezone


class BudgetExhausted(RuntimeError):
    pass


class ResumeLater(RuntimeError):
    def __init__(self, seconds):
        self.seconds = max(0, seconds)
        super().__init__(f"Rate limit cooldown: resume in at least {self.seconds:.1f} seconds")


def utc_day_start(now):
    return datetime.fromtimestamp(now, timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0).timestamp()


class Budget:
    def __init__(self, store, config):
        self.store, self.config = store, config

    def reserve(self, key, model, estimated_input, max_output, retry, now=None):
        now = time.time() if now is None else now
        limits = self.config["limits"] | self.config.get("model_limits", {}).get(model, {})
        reserved = estimated_input + max_output
        enforce_local = self.config.get("enforce_local_limits", True)
        if any(not isinstance(v, int) or v <= 0 for v in limits.values()) or self.config["daily_request_cap"] <= 0:
            raise ValueError("Budget limits must be positive integers")
        if enforce_local and reserved > limits["tokens_per_minute"]:
            raise BudgetExhausted("One request exceeds the configured TPM ceiling")
        db = self.store.db
        db.execute("BEGIN IMMEDIATE")
        try:
            cooldown = db.execute("SELECT until FROM cooldowns WHERE model=?", (model,)).fetchone()
            if cooldown and cooldown[0] > now:
                raise ResumeLater(cooldown[0] - now)
            rows = db.execute("SELECT * FROM attempts WHERE started>=?", (min(utc_day_start(now), now-60),)).fetchall()
            today = [r for r in rows if r["started"] >= utc_day_start(now)]
            model_today = [r for r in today if r["model"] == model]
            if enforce_local and (len(today) >= self.config["daily_request_cap"] or len(model_today) >= limits["requests_per_day"]):
                raise BudgetExhausted("Daily request ceiling reached; resume on the next UTC day")
            # Charge estimated maximum if usage is unknown (including failed/crashed requests).
            def tokens(row):
                return (row["input_tokens"] + row["output_tokens"]
                        if row["input_tokens"] is not None and row["output_tokens"] is not None else row["reserved_tokens"])
            if enforce_local and sum(map(tokens, model_today)) + reserved > limits["tokens_per_day"]:
                raise BudgetExhausted("Daily token ceiling reached; resume on the next UTC day")
            minute = [r for r in rows if r["model"] == model and r["started"] > now - 60]
            if enforce_local and (len(minute) >= limits["requests_per_minute"] or sum(map(tokens, minute)) + reserved > limits["tokens_per_minute"]):
                raise ResumeLater(min(r["started"] for r in minute) + 60.1 - now)
            cursor = db.execute("""INSERT INTO attempts
                (request_key,model,started,estimated_input,reserved_tokens,state,retry) VALUES (?,?,?,?,?,'in_flight',?)""",
                                (key, model, now, estimated_input, reserved, retry))
            db.commit()
            return cursor.lastrowid
        except BaseException:
            db.rollback()
            raise

    def summary(self, now=None):
        now = time.time() if now is None else now
        rows = self.store.db.execute("""SELECT model, COUNT(*) AS requests,
            SUM(estimated_input) AS estimated_input_tokens, SUM(input_tokens) AS actual_input_tokens,
            SUM(output_tokens) AS output_tokens, SUM(status=429) AS count_429,
            SUM(retry>0) AS retries, SUM(input_tokens IS NULL) AS unknown_usage_requests
            FROM attempts WHERE started>=? GROUP BY model ORDER BY model""", (utc_day_start(now),)).fetchall()
        return {"utc_date": datetime.fromtimestamp(now, timezone.utc).date().isoformat(),
                "requests_today": sum(row["requests"] for row in rows), "per_model": [dict(r) for r in rows]}

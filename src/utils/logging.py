import json
import os
from pathlib import Path

from src.utils.time import utc_now


def redact(text):
    key = os.environ.get("GROQ_API_KEY")
    return text.replace(key, "[REDACTED]") if key else text


def event(path, name, **details):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    record = dict(timestamp=utc_now(), level="INFO", event=name, **details)
    with Path(path).open("a", encoding="utf-8") as stream:
        stream.write(redact(json.dumps(record, ensure_ascii=False)) + "\n")
        stream.flush()

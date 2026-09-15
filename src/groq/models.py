import json
from datetime import datetime, timezone

from src.utils.io import project_path


def snapshot(client, folder):
    value = client.models()
    folder = project_path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc)
    path = folder / f"model_snapshot_{stamp:%Y%m%d}.json"
    if path.exists():
        path = folder / f"model_snapshot_{stamp:%Y%m%dT%H%M%S%fZ}.json"
    # Snapshot is append-only, including repeated checks on the same day.
    with path.open("x", encoding="utf-8") as stream:
        json.dump(dict(captured_at_utc=stamp.isoformat(), free_tier_access_verified=False,
                       response=value), stream, ensure_ascii=False, indent=2)
    return path, value


def require_models(value, requested):
    available = {row["id"] for row in value["data"] if row.get("active", True)}
    missing = sorted(set(requested) - available)
    if missing:
        raise RuntimeError("Configured Groq models unavailable; no silent substitution: " + ", ".join(missing))
    return sorted(set(requested))

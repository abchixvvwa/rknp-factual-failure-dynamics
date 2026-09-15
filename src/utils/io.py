import json
import os
import tempfile
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def atomic_write(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix=path.name, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        # Windows readers/virus scanners can briefly hold the destination open.
        for attempt in range(6):
            try:
                os.replace(temporary, path)
                break
            except PermissionError:
                if attempt == 5:
                    raise
                time.sleep(0.05 * 2**attempt)
    finally:
        Path(temporary).unlink(missing_ok=True)


def write_json(path, value):
    atomic_write(path, json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n")


def read_yaml(path):
    with Path(path).open(encoding="utf-8-sig") as stream:
        value = yaml.safe_load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"Expected YAML mapping: {path}")
    return value


def load_config(path=None):
    path = Path(path or ROOT / "configs/experiment.yaml").resolve()
    result = read_yaml(path)
    for name, filename in result.pop("config_files", {}).items():
        result[name] = read_yaml(path.parent / filename)
    if result["groq"]["base_url"] != "https://api.groq.com/openai/v1":
        raise ValueError("Only the official Groq inference endpoint is allowed")
    sampling = result["generation"]["sampling"]
    if sampling["count"] != len(sampling["seeds"]) or len(set(sampling["seeds"])) != sampling["count"]:
        raise ValueError("Sample count must match distinct configured seeds")
    if sampling["count"] != 5:
        raise ValueError("Protocol v1 requires five samples; amend the protocol before changing it")
    return result


def project_path(value):
    path = Path(value)
    return path if path.is_absolute() else ROOT / path

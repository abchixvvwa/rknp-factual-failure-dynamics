import json
import os
import sqlite3
import time
from contextlib import contextmanager
from pathlib import Path

from src.utils.hashing import stable_hash
from src.utils.io import write_json


class Store:
    """SQLite is the durable journal; Parquet is a reproducible export."""

    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.path, timeout=30)
        self.db.row_factory = sqlite3.Row
        self.db.executescript("""
            PRAGMA journal_mode=WAL;
            PRAGMA synchronous=FULL;
            PRAGMA foreign_keys=ON;
            CREATE TABLE IF NOT EXISTS experiments (
                id TEXT PRIMARY KEY, config_hash TEXT NOT NULL, metadata TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS requests (
                key TEXT PRIMARY KEY, spec TEXT NOT NULL, payload_hash TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS attempts (
                id INTEGER PRIMARY KEY, request_key TEXT NOT NULL REFERENCES requests(key),
                model TEXT NOT NULL, started REAL NOT NULL, estimated_input INTEGER NOT NULL,
                reserved_tokens INTEGER NOT NULL, state TEXT NOT NULL, status INTEGER,
                input_tokens INTEGER, output_tokens INTEGER, retry INTEGER NOT NULL,
                record TEXT);
            CREATE UNIQUE INDEX IF NOT EXISTS unique_success ON attempts(request_key)
                WHERE state='success';
            CREATE INDEX IF NOT EXISTS budget_window ON attempts(started, model);
            CREATE TABLE IF NOT EXISTS cooldowns (model TEXT PRIMARY KEY, until REAL NOT NULL);
        """)

    def close(self):
        self.db.close()

    @contextmanager
    def writer_lock(self):
        """OS releases this single-runner lock on crash; readers remain available."""
        path = self.path.with_suffix(".runner.lock")
        with path.open("a+b") as stream:
            stream.seek(0)
            if not stream.read(1):
                stream.write(b"0")
                stream.flush()
            stream.seek(0)
            if os.name == "nt":
                import msvcrt
                try:
                    msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                except OSError as exc:
                    raise RuntimeError("Another generation runner is active") from exc
            else:
                import fcntl
                fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
            try:
                yield
            finally:
                stream.seek(0)
                if os.name == "nt":
                    msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    fcntl.flock(stream, fcntl.LOCK_UN)

    def register_experiment(self, experiment_id, immutable, metadata):
        digest = stable_hash(immutable)
        existing = self.db.execute("SELECT config_hash FROM experiments WHERE id=?", (experiment_id,)).fetchone()
        if existing and existing[0] != digest:
            raise ValueError("Experiment inputs changed. Restore them or use a new experiment ID")
        with self.db:
            self.db.execute("INSERT OR IGNORE INTO experiments VALUES (?,?,?)",
                            (experiment_id, digest, json.dumps(metadata, ensure_ascii=False)))

    def register(self, spec):
        identity = [spec[k] for k in ("experiment_id", "fact_id", "language", "model_id",
                                     "generation_type", "sample_index", "prompt_version")]
        key = stable_hash(identity)
        payload_hash = stable_hash(spec)
        old = self.db.execute("SELECT payload_hash FROM requests WHERE key=?", (key,)).fetchone()
        if old and old[0] != payload_hash:
            raise ValueError("Request key reused with different prompt or parameters")
        with self.db:
            self.db.execute("INSERT OR IGNORE INTO requests VALUES (?,?,?)",
                            (key, json.dumps(spec, ensure_ascii=False), payload_hash))
        return key

    def success(self, key):
        row = self.db.execute("SELECT record FROM attempts WHERE request_key=? AND state='success'", (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def check_uncertain(self, key):
        row = self.db.execute("SELECT id FROM attempts WHERE request_key=? AND state='in_flight'", (key,)).fetchone()
        if row:
            raise RuntimeError(f"Interrupted in-flight attempt {row[0]}; inspect it before --retry-uncertain")

    def release_uncertain(self, key):
        with self.db:
            self.db.execute("UPDATE attempts SET state='uncertain' WHERE request_key=? AND state='in_flight'", (key,))

    def finish(self, attempt, state, record, status=None, usage=None):
        usage = usage or {}
        with self.db:
            self.db.execute("""UPDATE attempts SET state=?, status=?, input_tokens=?, output_tokens=?, record=?
                               WHERE id=? AND state='in_flight'""",
                            (state, status, usage.get("prompt_tokens"), usage.get("completion_tokens"),
                             json.dumps(record, ensure_ascii=False), attempt))

    def defer(self, model, seconds, now=None):
        until = (time.time() if now is None else now) + seconds
        with self.db:
            self.db.execute("""INSERT INTO cooldowns VALUES (?,?) ON CONFLICT(model)
                               DO UPDATE SET until=MAX(until,excluded.until)""", (model, until))

    def export(self, path):
        import pandas as pd

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        rows = [json.loads(r[0]) for r in self.db.execute("SELECT record FROM attempts WHERE state='success' ORDER BY id")]
        if rows:
            # Parquet cannot merge evolving nested JSON schemas across resumed runs.
            # Keep complex audit fields losslessly as JSON strings.
            for row in rows:
                for key, value in row.items():
                    if isinstance(value, (dict, list)):
                        row[key] = json.dumps(value, ensure_ascii=False, sort_keys=True)
            temporary = path.with_suffix(".tmp.parquet")
            pd.DataFrame(rows).to_parquet(temporary, index=False)
            os.replace(temporary, path)
        failed = [dict(r) for r in self.db.execute("SELECT * FROM attempts WHERE state!='success' ORDER BY id")]
        write_json(path.with_name("failed_attempts.json"), failed)
        progress = dict(self.db.execute("SELECT state, count(*) FROM attempts GROUP BY state").fetchall())
        write_json(path.with_name("progress.json"), progress)
        return progress

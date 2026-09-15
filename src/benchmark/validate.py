import csv
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

from pydantic import ValidationError

from src.benchmark.schema import Fact
from src.utils.hashing import file_hash


def read_benchmark(path, main=False):
    facts, errors, seen = [], [], set()
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None or set(reader.fieldnames) != set(Fact.model_fields):
            raise ValueError("Benchmark CSV must contain exactly the documented columns")
        if len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError("Duplicate CSV column names")
        for line, row in enumerate(reader, 2):
            try:
                fact = Fact.model_validate(row)
                if fact.fact_id in seen:
                    raise ValueError(f"Duplicate fact_id: {fact.fact_id}")
                if main and not fact.verified_by_human:
                    raise ValueError(f"Main fact {fact.fact_id} is not human-verified")
                seen.add(fact.fact_id)
                facts.append(fact)
            except (ValueError, ValidationError) as exc:
                errors.append(f"Row {line}: {exc}")
    if errors:
        raise ValueError("\n".join(errors))
    if not facts:
        raise ValueError("Benchmark is empty; add sourced facts before generating or splitting")
    return sorted(facts, key=lambda fact: fact.fact_id)


def source_checks(facts):
    """Availability checks are evidence of reachability, never human verification."""
    checks = {}
    for fact in facts:
        url = str(fact.source_url)
        if url in checks:
            continue
        request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "RKNP-source-check/1.0"})
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                checks[url] = dict(status=response.status, final_url=response.url)
        except urllib.error.HTTPError as exc:
            checks[url] = dict(status=exc.code, needs_manual_check=True)
        except (OSError, urllib.error.URLError):
            checks[url] = dict(status=None, needs_manual_check=True)
    return checks


def summary(path, facts):
    return dict(benchmark_sha256=file_hash(path), fact_count=len(facts),
                language_prompts=3 * len(facts), categories=dict(Counter(f.category for f in facts)),
                human_verified=sum(f.verified_by_human for f in facts))

import csv
import io
import math
import random
from collections import Counter, defaultdict

from src.utils.hashing import stable_hash
from src.utils.io import atomic_write


def make_splits(facts, proportions=None, seed=42):
    """Exact global quotas; greedy proportional allocation within categories."""
    proportions = proportions or dict(train=.70, validation=.15, test=.15)
    names = list(proportions)
    if set(names) != {"train", "validation", "test"} or any(v <= 0 for v in proportions.values()):
        raise ValueError("Three positive train/validation/test proportions are required")
    if not math.isclose(sum(proportions.values()), 1):
        raise ValueError("Split proportions must sum to one")
    if len(facts) < 3 or len({f.fact_id for f in facts}) != len(facts):
        raise ValueError("Need at least three distinct facts")
    desired = {name: len(facts) * proportions[name] for name in names}
    quotas = {name: math.floor(desired[name]) for name in names}
    for name in sorted(names, key=lambda n: (-(desired[n] - quotas[n]), names.index(n)))[:len(facts) - sum(quotas.values())]:
        quotas[name] += 1
    if not all(quotas.values()):
        raise ValueError("Dataset too small to populate all splits at these proportions")
    groups = defaultdict(list)
    for fact in facts:
        groups[fact.category].append(fact.fact_id)
    allocated, rows = Counter(), []
    # Interleave categories, so the last category does not absorb all quota error.
    decks = {}
    for category, ids in sorted(groups.items()):
        deck = sorted(ids)
        random.Random(stable_hash([seed, category])).shuffle(deck)
        decks[category] = deck
    local = defaultdict(Counter)
    for round_index in range(max(map(len, decks.values()))):
        for category, ids in decks.items():
            if round_index >= len(ids):
                continue
            available = [name for name in names if allocated[name] < quotas[name]]
            chosen = max(available, key=lambda n: ((round_index + 1) * proportions[n] - local[category][n],
                                                   quotas[n] - allocated[n], -names.index(n)))
            rows.append(dict(fact_id=ids[round_index], split=chosen))
            local[category][chosen] += 1
            allocated[chosen] += 1
    rows.sort(key=lambda row: row["fact_id"])
    assert {r["fact_id"] for r in rows} == {f.fact_id for f in facts}
    assert dict(allocated) == quotas
    return rows


def save_splits(path, rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=["fact_id", "split"], lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    atomic_write(path, stream.getvalue())

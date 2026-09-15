from collections import Counter

from src.benchmark.schema import Fact, CATEGORIES
from src.benchmark.split import make_splits


def test_deterministic_no_leakage_balanced(fact_row):
    facts = []
    for category, count in zip(CATEGORIES, [80, 80, 80, 80, 80, 100]):
        for i in range(count):
            row = dict(fact_row, fact_id=f"{category}_{i:03}", category=category)
            if category == "adversarial_false_premise":
                row.update(false_premise=True, question_type="false_premise")
            facts.append(Fact.model_validate(row))
    rows = make_splits(facts)
    assert rows == make_splits(list(reversed(facts)))
    assert rows != make_splits(facts, seed=99)
    assert len(rows) == len({r["fact_id"] for r in rows}) == 500
    assert {r["fact_id"] for r in rows} == {f.fact_id for f in facts}
    assert Counter(r["split"] for r in rows) == dict(train=350, validation=75, test=75)
    categories = {f.fact_id: f.category for f in facts}
    for category, count in zip(CATEGORIES, [80, 80, 80, 80, 80, 100]):
        distribution = Counter(r["split"] for r in rows if categories[r["fact_id"]] == category)
        for name, proportion in dict(train=.7, validation=.15, test=.15).items():
            assert abs(distribution[name] - count * proportion) <= 2


def test_small_smoke_dataset(fact_row):
    facts = [Fact.model_validate(dict(fact_row, fact_id=str(i))) for i in range(10)]
    assert Counter(r["split"] for r in make_splits(facts)) == dict(train=7, validation=2, test=1)

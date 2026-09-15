import csv
from datetime import date

import pytest

from src.benchmark.schema import Fact
from src.utils.io import load_config


@pytest.fixture
def config():
    return load_config()


@pytest.fixture
def fact_row():
    # Synthetic unit fixture; never exported as research evidence.
    return dict(fact_id="fixture_1", category="science", difficulty="test", question_type="entity",
                question_en="Fixture EN?", question_ru="Fixture RU?", question_kk="Fixture KK?",
                canonical_answer="Fixture", acceptable_aliases_json='["Alias"]', false_premise=False,
                source_url="https://example.org/fixture", source_title="Unit test fixture",
                source_publisher="Test", source_accessed_date=date.today().isoformat(),
                notes="Not research data", verified_by_human=False)


@pytest.fixture
def write_facts(tmp_path):
    def write(rows):
        path = tmp_path / "facts.csv"
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=Fact.model_fields)
            writer.writeheader()
            writer.writerows(rows)
        return path
    return write


@pytest.fixture
def spec():
    return dict(experiment_id="unit_test", fact_id="fixture_1", language="en", model_id="test_model",
                generation_type="target", sample_index=0, prompt_version="test_v1", prompt_text="Fixture?",
                parameters=dict(temperature=0.0, seed=42, max_completion_tokens=96))

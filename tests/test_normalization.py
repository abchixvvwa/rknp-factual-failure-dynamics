import pytest

from src.benchmark.schema import Fact
from src.labeling.normalize import normalize
from src.labeling.exact_match import exact_match
from src.labeling.numeric_match import numeric_match
from src.labeling.date_match import date_match
from src.labeling.build_labels import automatic_label


def test_unicode_casing_and_negation():
    assert normalize("  ＭＥＲＣＵＲＹ. ") == "mercury"
    assert exact_match("МЕРКУРИЙ.", "Mercury", ["Меркурий"])
    assert not exact_match("Not Mercury", "Mercury")
    assert not exact_match("-5", "5")
    assert not exact_match("5%", "5")
    assert not exact_match("It is Mercury or Venus", "Mercury")


@pytest.mark.parametrize("a,b,expected", [("1 234", "1234", True), ("1,5", "1.50", True),
    ("−5", "5", False), ("1,234", "1234", None), ("5 km", "5", None)])
def test_numbers(a, b, expected):
    assert numeric_match(a, b) is expected


@pytest.mark.parametrize("text", ["July 4, 1776", "4 июля 1776 года", "1776 жылғы 4 шілде", "1776-07-04"])
def test_dates(text):
    assert date_match(text, "1776-07-04") is True
    assert date_match("04/07/1776", "1776-07-04") is None


def test_unmatched_entity_is_not_automatically_wrong(fact_row):
    label = automatic_label(Fact.model_validate(fact_row), "An answer with extra context")
    assert label["label_status"] == "unresolved" and label["is_factually_correct"] is None

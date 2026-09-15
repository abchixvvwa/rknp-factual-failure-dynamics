import pytest

from src.benchmark.schema import Fact
from src.labeling.build_labels import build_labels


def test_review_is_linked_to_actual_response(fact_row):
    case = dict(case_id="case", fact_id="fixture_1", language="en", model_id="unit", question="Fixture?",
                fact=Fact.model_validate(fact_row), complete=True,
                target=dict(request_id="request", response_sha256="hash", valid_response=True, response_text="Unknown"))
    assert build_labels([case])[0]["label_status"] == "unresolved"
    review = dict(request_id="request", response_sha256="hash", review_label="0", reviewer="human")
    assert build_labels([case], [review])[0]["label_status"] == "manual_incorrect"
    with pytest.raises(ValueError, match="hash mismatch"):
        build_labels([case], [dict(review, response_sha256="stale")])
    with pytest.raises(ValueError, match="reviewer"):
        build_labels([case], [dict(review, reviewer="")])

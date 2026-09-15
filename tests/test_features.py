import pandas as pd
import pytest

from src.features.schema import PREDICTOR_COLUMNS, validate_features


def test_feature_contract_blocks_leakage_and_label_inversion():
    row = dict.fromkeys(PREDICTOR_COLUMNS, 0.0)
    row.update(case_id="unit", fact_id="fact", language="en", target_model="fixture", split="train",
               is_factually_correct=1, error_label=0, n_clusters=1)
    validate_features(pd.DataFrame([row]))
    with pytest.raises(ValueError, match="orientation"):
        validate_features(pd.DataFrame([dict(row, error_label=1)]))
    with pytest.raises(ValueError, match="leakage"):
        validate_features(pd.DataFrame([row, dict(row, case_id="other", language="ru", split="test")]))
    with pytest.raises(ValueError, match="Non-finite"):
        validate_features(pd.DataFrame([dict(row, entropy_slope=float("nan"))]))

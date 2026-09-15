from types import SimpleNamespace

import joblib
import numpy as np
import pandas as pd
import pytest

from src.features.schema import PREDICTOR_COLUMNS
from src.modeling.baselines import candidates
from src.modeling.calibration import fit_calibrators
from src.modeling.train import development_data, select_validation, train_family


def fixture_frame():
    rows = []
    for fact in range(120):
        for language in ("en", "ru"):
            error = fact % 2
            row = dict.fromkeys(PREDICTOR_COLUMNS, 0.0)
            row.update(case_id=f"{fact}-{language}", fact_id=f"f{fact}", language=language, target_model="fixture",
                       split="train" if fact < 84 else "validation" if fact < 102 else "test",
                       error_label=error, is_factually_correct=1-error, n_clusters=1+error,
                       semantic_entropy=.5*error, unique_normalized_answers=1+error,
                       target_support_ratio=1-error, entropy_slope=.1*error)
            rows.append(row)
    return pd.DataFrame(rows)


def test_test_values_are_not_loaded_and_facts_cannot_leak(tmp_path):
    frame = fixture_frame()
    frame.loc[frame.split == "test", PREDICTOR_COLUMNS + ["error_label"]] = np.nan
    path = tmp_path / "features.parquet"
    frame.to_parquet(path)
    train, val = development_data(path)
    assert len(train) == 168 and len(val) == 36
    assert set(train.fact_id).isdisjoint(val.fact_id)
    frame.loc[0, "fact_id"] = "f110"
    frame.to_parquet(path)
    with pytest.raises(ValueError, match="leakage"):
        development_data(path)


def test_smoke_and_unresolved_labels_are_blocked(tmp_path):
    path = tmp_path / "features.parquet"
    frame = fixture_frame()
    frame.head(20).to_parquet(path)
    with pytest.raises(ValueError, match="smoke"):
        development_data(path)
    frame.loc[0, ["error_label", "is_factually_correct"]] = np.nan
    frame.to_parquet(path)
    with pytest.raises(ValueError, match="Resolve"):
        development_data(path)


def test_calibration_holds_out_whole_facts():
    train = fixture_frame().query("split == 'train'")
    estimator, columns = candidates("dynamic")["dynamic_logistic"]
    _, folds = fit_calibrators(estimator, train[columns], train.error_label, train.fact_id)
    assert pd.DataFrame(dict(fact=train.fact_id, fold=folds)).groupby("fact").fold.nunique().max() == 1
    assert len(set(folds)) == 5


def test_training_selection_and_tamper_detection(tmp_path, monkeypatch):
    import src.modeling.train as module
    monkeypatch.setattr(module, "project_path", lambda value: tmp_path / value)
    path = tmp_path / "artifacts/features/unit/features.parquet"
    path.parent.mkdir(parents=True)
    fixture_frame().to_parquet(path)
    args = SimpleNamespace(experiment_id="unit", limit=None, dry_run=False)
    baseline = train_family(args, {"seed": 42}, "baselines")
    dynamic = train_family(args, {"seed": 42}, "dynamic")
    assert len(baseline["candidates"]) == 6 and len(dynamic["candidates"]) == 3
    model_path = tmp_path / "artifacts/models/unit/dynamic/models.joblib"
    bundles = joblib.load(model_path)
    scaler = bundles["dynamic_logistic"]["estimator"].steps[0][1]
    train = fixture_frame().query("split == 'train'")
    np.testing.assert_allclose(scaler.mean_, train[bundles["dynamic_logistic"]["columns"]].mean())
    selection = select_validation(args, {"seed": 42})
    assert not selection["test_evaluated"]
    with pytest.raises(ValueError, match="already saved"):
        select_validation(args, {"seed": 42})
    model_path.write_bytes(b"changed")
    with pytest.raises(ValueError, match="changed"):
        select_validation(args, {"seed": 42})

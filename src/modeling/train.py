import json

import joblib
import pandas as pd
from sklearn.calibration import calibration_curve

from src.evaluation.metrics import metrics, select_threshold
from src.features.schema import validate_features
from src.modeling.baselines import candidates
from src.modeling.calibration import calibrated_probability, fit_calibrators
from src.utils.hashing import file_hash
from src.utils.io import project_path, write_json
from src.utils.reproducibility import metadata


def development_data(path, minimum_facts=100):
    # Inspect assignment metadata globally; never load test predictors or labels.
    identity = pd.read_parquet(path, columns=["fact_id", "case_id", "split"])
    if identity.case_id.duplicated().any() or (identity.groupby("fact_id").split.nunique() > 1).any():
        raise ValueError("Duplicate case or fact leakage across splits")
    if not identity.split.isin(["train", "validation", "test"]).all():
        raise ValueError("Unknown split")
    if identity.fact_id.nunique() < minimum_facts:
        raise ValueError(f"Scientific training requires at least {minimum_facts} feature-bearing facts; smoke data cannot qualify")
    frame = validate_features(pd.read_parquet(path, filters=[("split", "in", ["train", "validation"])]))
    if frame.error_label.isna().any():
        raise ValueError("Resolve all included train/validation target labels before training")
    train, validation = (frame.loc[frame.split == split].copy() for split in ("train", "validation"))
    for split, subset in (("train", train), ("validation", validation)):
        if set(subset.error_label.unique()) != {0, 1}:
            raise ValueError(f"{split} needs both correct and incorrect targets")
    return train, validation


def train_family(args, config, family):
    if args.limit:
        raise ValueError("Scientific training does not accept partial --limit runs")
    path = project_path("artifacts/features") / args.experiment_id / "features.parquet"
    train, validation = development_data(path)
    folder = project_path("artifacts/models") / args.experiment_id / family
    if folder.exists() and not args.dry_run:
        raise ValueError("Model output already exists; use a new experiment ID for changed research inputs")
    report = dict(experiment_id=args.experiment_id, family=family, features_sha256=file_hash(path),
                  train_rows=len(train), validation_rows=len(validation), test_access="assignment metadata only",
                  seed=config["seed"], calibration_fit="grouped out-of-fold train scores",
                  threshold_criterion="max_f1", candidates={}, provenance=metadata(args.experiment_id, config))
    if args.dry_run:
        return report
    bundles = {}
    for name, (estimator, columns) in candidates(family, config["seed"]).items():
        X, y = train[columns], train.error_label.astype(int)
        calibrators, folds = fit_calibrators(estimator, X, y, train.fact_id, config["seed"])
        estimator.fit(X, y)
        raw = estimator.predict_proba(validation[columns])[:, 1]
        variants = {}
        for method, calibrator in calibrators.items():
            probability = calibrated_probability(calibrator, method, raw)
            threshold = select_threshold(validation.error_label, probability)
            observed, predicted = calibration_curve(validation.error_label, probability, n_bins=10, strategy="uniform")
            variants[method] = dict(metrics=metrics(validation.error_label, probability, threshold), threshold=threshold,
                                    calibration_curve=dict(observed=observed.tolist(), predicted=predicted.tolist()))
        # Calibration selected by validation Brier; ties prefer raw, then sigmoid.
        selected = min(variants, key=lambda method: variants[method]["metrics"]["brier"])
        report["candidates"][name] = dict(columns=columns, estimator=repr(estimator), variants=variants, selected_calibration=selected)
        bundles[name] = dict(estimator=estimator, columns=columns, calibrators=calibrators,
                             selected_calibration=selected, threshold=variants[selected]["threshold"])
        report["candidates"][name]["calibration_folds"] = dict(zip(train.case_id, folds.tolist()))
    folder.mkdir(parents=True)
    joblib.dump(bundles, folder / "models.joblib")
    report["model_sha256"] = file_hash(folder / "models.joblib")
    write_json(folder / "validation.json", report)
    return report


def select_validation(args, config):
    if args.limit:
        raise ValueError("Model selection does not accept --limit")
    folder = project_path("artifacts/models") / args.experiment_id
    reports = [json.loads((folder / family / "validation.json").read_text(encoding="utf-8")) for family in ("baselines", "dynamic")]
    features = project_path("artifacts/features") / args.experiment_id / "features.parquet"
    for family, report in zip(("baselines", "dynamic"), reports):
        if report["features_sha256"] != file_hash(features) or report["model_sha256"] != file_hash(folder / family / "models.joblib"):
            raise ValueError("Training artifact changed after validation")
    dynamic = reports[1]["candidates"]
    selected = max(dynamic, key=lambda name: dynamic[name]["variants"][dynamic[name]["selected_calibration"]]["metrics"]["auroc"])
    candidate = dynamic[selected]
    method = candidate["selected_calibration"]
    result = dict(experiment_id=args.experiment_id, selected_model=selected, calibration=method,
                  threshold=candidate["variants"][method]["threshold"], primary_metric="auroc",
                  features_sha256=file_hash(features), model_sha256=reports[1]["model_sha256"],
                  selection_data="validation only", test_evaluated=False,
                  validation_reports={family: file_hash(folder / family / "validation.json") for family in ("baselines", "dynamic")})
    destination = folder / "selection.json"
    if not args.dry_run:
        if destination.exists():
            raise ValueError("Selection already saved; do not overwrite frozen model choices")
        write_json(destination, result)
    return result

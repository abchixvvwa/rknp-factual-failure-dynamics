import json

import joblib
import pandas as pd

from _common import main, parser
from src.evaluation.bootstrap import bootstrap
from src.evaluation.metrics import metrics
from src.modeling.calibration import calibrated_probability
from src.utils.hashing import file_hash
from src.utils.io import project_path, write_json


def probability(bundle, frame):
    raw = bundle["estimator"].predict_proba(frame[bundle["columns"]])[:, 1]
    method = bundle["selected_calibration"]
    return calibrated_probability(bundle["calibrators"][method], method, raw)


def run(args, config):
    if args.limit:
        raise ValueError("Final test evaluation does not accept --limit")
    model_folder = project_path("artifacts/models") / args.experiment_id
    selection_path = model_folder / "selection.json"
    destination = project_path("results/reports") / f"{args.experiment_id}_test_metrics.json"
    predictions_path = project_path("artifacts/predictions") / args.experiment_id / "test_predictions.parquet"
    if destination.exists() or predictions_path.exists():
        raise ValueError("Test was already evaluated; refusing to overwrite the one-time result")
    selection = json.loads(selection_path.read_text(encoding="utf-8"))
    if selection.get("test_evaluated") is not False:
        raise ValueError("Selection artifact does not authorize first test evaluation")
    features_path = project_path("artifacts/features") / args.experiment_id / "features.parquet"
    frame = pd.read_parquet(features_path)
    test = frame.loc[frame.split == "test"].copy()
    if test.empty or test.error_label.isna().any():
        raise ValueError("Complete labeled test rows required")

    dynamic_bundles = joblib.load(model_folder / "dynamic" / "models.joblib")
    selected = dynamic_bundles[selection["selected_model"]]
    if selected["selected_calibration"] != selection["calibration"] or selected["threshold"] != selection["threshold"]:
        raise ValueError("Frozen selection and model bundle disagree")
    test["risk_probability"] = probability(selected, test)

    baseline_bundles = joblib.load(model_folder / "baselines" / "models.joblib")
    static = baseline_bundles["B4_static"]
    test["static_probability"] = probability(static, test)
    y = test.error_label.astype(int).to_numpy()
    threshold = float(selection["threshold"])
    result = {
        "experiment_id": args.experiment_id,
        "one_time_test_evaluation": True,
        "selected_model": selection["selected_model"],
        "calibration": selection["calibration"],
        "threshold": threshold,
        "features_sha256": file_hash(features_path),
        "selection_sha256": file_hash(selection_path),
        "overall": metrics(y, test.risk_probability, threshold),
        "static_comparator": metrics(y, test.static_probability, static["threshold"]),
        "bootstrap": bootstrap(
            y,
            test.risk_probability,
            test.fact_id,
            resamples=config["bootstrap"]["resamples"],
            confidence=config["bootstrap"]["confidence_level"],
            seed=config["seed"],
            paired_scores=test.static_probability,
            threshold=threshold,
        ),
        "slices": {},
    }
    for column in ("language", "target_model", "category"):
        result["slices"][column] = {
            str(name): metrics(group.error_label.astype(int), group.risk_probability, threshold)
            for name, group in test.groupby(column, sort=True)
        }
    result["language_model_matrix"] = {
        str(model): {
            str(language): metrics(group.error_label.astype(int), group.risk_probability, threshold)
            for language, group in model_rows.groupby("language", sort=True)
        }
        for model, model_rows in test.groupby("target_model", sort=True)
    }
    if not args.dry_run:
        predictions_path.parent.mkdir(parents=True, exist_ok=True)
        test[["case_id", "fact_id", "language", "target_model", "category", "error_label",
              "risk_probability", "static_probability"]].to_parquet(predictions_path, index=False)
        result["predictions_sha256"] = file_hash(predictions_path)
        write_json(destination, result)
    return result


if __name__ == "__main__":
    main(run, parser("Evaluate the frozen selected model on test exactly once"))

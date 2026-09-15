"""Read-only verification of the published pilot100_v1 release."""

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    features_path = ROOT / "artifacts/features/pilot100_v1/features.parquet"
    metrics_path = ROOT / "results/reports/pilot100_v1_test_metrics.json"
    predictions_path = ROOT / "artifacts/predictions/pilot100_v1/test_predictions.parquet"
    semantics = ROOT / "artifacts/semantic_judgments/pilot100_v1/semantic_v4_joint"
    review_queue = ROOT / "data/labels/pilot100_v1/semantic_review_queue.csv"

    required = [features_path, metrics_path, predictions_path, semantics, review_queue]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        raise SystemExit("Missing release artifacts: " + ", ".join(missing))

    features = pd.read_parquet(features_path)
    predictions = pd.read_parquet(predictions_path)
    review = pd.read_csv(review_queue)
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    semantic_count = sum(
        path.stem.isalnum() and len(path.stem) == 64
        for path in semantics.glob("*.json")
    )

    observed = {
        "semantic_cases": semantic_count,
        "feature_rows": len(features),
        "split_counts": features["split"].value_counts().sort_index().to_dict(),
        "test_rows": len(predictions),
        "test_errors": int(predictions["error_label"].sum()),
        "semantic_review_cases": len(review),
        "dynamic_auroc": metrics["overall"]["auroc"],
        "dynamic_auprc": metrics["overall"]["auprc"],
        "static_auroc": metrics["static_comparator"]["auroc"],
    }
    expected = {
        "semantic_cases": 866,
        "feature_rows": 832,
        "split_counts": {"test": 131, "train": 574, "validation": 127},
        "test_rows": 131,
        "test_errors": 24,
        "semantic_review_cases": 200,
    }
    for key, value in expected.items():
        if observed[key] != value:
            raise SystemExit(f"Release verification failed: {key}={observed[key]!r}, expected {value!r}")
    print(json.dumps({"status": "pass", **observed}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

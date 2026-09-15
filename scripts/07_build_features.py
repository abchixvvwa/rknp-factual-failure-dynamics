import csv
import json

import pandas as pd

from _common import main, parser
from src.features.build import build_case_features
from src.features.schema import validate_features
from src.semantics.judge import JUDGE_VERSION
from src.utils.cases import load_cases
from src.utils.hashing import file_hash
from src.utils.io import project_path, write_json


def run(args, config):
    cases = load_cases(config, args.experiment_id)
    if args.limit:
        ids = sorted({c["fact_id"] for c in cases})[:args.limit]
        cases = [c for c in cases if c["fact_id"] in ids]
    splits_path = project_path(config["paths"]["splits"])
    with splits_path.open(encoding="utf-8", newline="") as stream:
        assignments = list(csv.DictReader(stream))
    splits = {row["fact_id"]: row["split"] for row in assignments}
    if len(splits) != len(assignments) or any(s not in ("train", "validation", "test") for s in splits.values()):
        raise ValueError("Invalid or duplicated split assignment")
    labels_path = project_path("data/labels") / args.experiment_id / "labels.csv"
    with labels_path.open(encoding="utf-8", newline="") as stream:
        labels = {r["case_id"]: r for r in csv.DictReader(stream)}
    rows, excluded = [], []
    for case in cases:
        grouping_path = project_path("artifacts/semantic_judgments") / args.experiment_id / JUDGE_VERSION / f"{case['case_id']}.json"
        if not case["complete"] or not grouping_path.exists():
            excluded.append(dict(case_id=case["case_id"], reason="Incomplete generations or missing grouping"))
            continue
        grouping = json.loads(grouping_path.read_text(encoding="utf-8"))
        if any(p["uncertain"] for p in grouping["prefixes"]):
            excluded.append(dict(case_id=case["case_id"], reason="Judge uncertainty requires human review"))
            continue
        row = build_case_features(case, grouping, labels[case["case_id"]], splits[case["fact_id"]])
        row.update(benchmark_sha256=file_hash(project_path(config["paths"]["benchmark"])),
                   grouping_sha256=file_hash(grouping_path), split_sha256=file_hash(splits_path),
                   labels_sha256=file_hash(labels_path), experiment_id=args.experiment_id)
        rows.append(row)
    report = dict(observed_cases=len(cases), feature_rows=len(rows), excluded=excluded,
                  unresolved_labels=sum(r["error_label"] is None for r in rows),
                  note="No predictive metrics are computed from engineering smoke data")
    frame = validate_features(pd.DataFrame(rows)) if rows else None
    if not args.dry_run:
        folder = project_path("artifacts/features") / args.experiment_id
        folder.mkdir(parents=True, exist_ok=True)
        if rows:
            frame.to_parquet(folder / "features.parquet", index=False)
        write_json(project_path("results/reports") / f"{args.experiment_id}_data_quality.json", report)
    return report


if __name__ == "__main__":
    main(run, parser("Build auditable features from complete cases only"))

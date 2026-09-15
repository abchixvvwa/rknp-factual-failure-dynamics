import csv

from _common import main, parser
from src.labeling.build_labels import build_labels
from src.labeling.manual_queue import manual_queue, write_rows
from src.utils.cases import load_cases
from src.utils.io import project_path, write_json


def run(args, config):
    cases = load_cases(config, args.experiment_id)
    if args.limit:
        cases = [c for c in cases if c["fact_id"] in sorted({c["fact_id"] for c in cases})[:args.limit]]
    reviewed = project_path("data/labels/reviewed_labels.csv")
    reviews = []
    if reviewed.exists():
        with reviewed.open(encoding="utf-8-sig", newline="") as stream:
            reviews = list(csv.DictReader(stream))
    rows = build_labels(cases, reviews)
    if not rows:
        raise ValueError("No target responses in the requested experiment")
    report = dict(cases=len(cases), targets=len(rows), complete_cases=sum(c["complete"] for c in cases),
                  resolved=sum(r["label_status"] != "unresolved" for r in rows),
                  unresolved=sum(r["label_status"] == "unresolved" for r in rows))
    if not args.dry_run:
        folder = project_path("data/labels") / args.experiment_id
        write_rows(folder / "labels.csv", rows, list(rows[0]))
        manual_queue(folder / "manual_review_queue.csv", rows)
        # Top-level queue is a convenience view; authoritative files are per experiment.
        manual_queue(project_path("data/labels/manual_review_queue.csv"), rows)
        write_json(project_path("results/reports") / f"{args.experiment_id}_labeling.json", report)
    return report


if __name__ == "__main__":
    main(run, parser("Build factual labels and explicit unresolved review queue"))

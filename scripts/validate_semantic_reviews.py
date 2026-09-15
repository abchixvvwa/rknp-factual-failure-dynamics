import csv
import json

from _common import main, parser
from src.semantics.judge import JUDGE_VERSION
from src.semantics.validate_judge import agreement
from src.utils.hashing import file_hash
from src.utils.io import project_path, write_json


def run(args, config):
    path = project_path("data/labels") / args.experiment_id / "semantic_review_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reviews = list(csv.DictReader(stream))
    completed = [r for r in reviews if r["human_groups_json"].strip()]
    if not args.smoke_preview and len(completed) < 200:
        raise ValueError(f"Need at least 200 completed human semantic reviews; got {len(completed)}")
    if not completed:
        raise ValueError("No human semantic annotations are completed")
    if len({r["case_id"] for r in completed}) != len(completed):
        raise ValueError("Duplicate reviewed case IDs")
    results = []
    for row in completed:
        human = json.loads(row["human_groups_json"])
        if not row["reviewer"].strip() or not isinstance(human, list) or len(human) != 5 or any(type(v) is not int for v in human):
            raise ValueError("Each annotation needs five integer labels and a named reviewer")
        grouping_file = project_path("artifacts/semantic_judgments") / args.experiment_id / JUDGE_VERSION / f"{row['case_id']}.json"
        grouping = json.loads(grouping_file.read_text(encoding="utf-8"))
        final = grouping["prefixes"][-1]
        labels = [None]*5
        for group_id, members in enumerate(final["groups"]):
            for member in members:
                labels[member] = group_id
        if any(label is None for label in labels):
            raise ValueError("Incomplete machine grouping")
        prefix_agreement = []
        for prefix in grouping["prefixes"]:
            predicted = [None]*prefix["k"]
            for group_id, members in enumerate(prefix["groups"]):
                for member in members:
                    predicted[member] = group_id
            prefix_agreement.append(dict(k=prefix["k"], **agreement(predicted, human[:prefix["k"]])))
        results.append(dict(case_id=row["case_id"], language=row["language"], model_id=row["model_id"],
                            category=row["category"], reviewer=row["reviewer"], judge_uncertain=final["uncertain"],
                            prefix_agreement=prefix_agreement,
                            **agreement(labels, human)))
    result = dict(cases=len(results), engineering_only=args.smoke_preview, judge_version=JUDGE_VERSION,
                  annotations_sha256=file_hash(path),
                  mean_ari=sum(r["adjusted_rand_index"] for r in results)/len(results),
                  pairwise_agreement=sum(r["pairwise_agreement"] for r in results)/len(results),
                  exact_cluster_match_rate=sum(r["exact_cluster_match"] for r in results)/len(results),
                  prefix_mean_ari={str(k): sum(r["prefix_agreement"][k-2]["adjusted_rand_index"] for r in results)/len(results)
                                   for k in range(2, 6)},
                  cases_detail=results,
                  note="Agreement acceptance thresholds must be fixed before main; no automatic approval from this report")
    if not args.dry_run:
        write_json(project_path("results/reports") / f"{args.experiment_id}_judge_validation.json", result)
    return result


if __name__ == "__main__":
    p = parser("Compare blinded human partitions with saved semantic judge groups")
    p.add_argument("--smoke-preview", action="store_true", help="Engineering-only analysis of fewer than 200 cases")
    main(run, p)

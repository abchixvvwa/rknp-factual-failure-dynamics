import json
import random
from collections import defaultdict

from _common import main, parser
from src.labeling.manual_queue import write_rows
from src.utils.cases import load_cases
from src.utils.io import project_path, write_json


def run(args, config):
    cases = [c for c in load_cases(config, args.experiment_id) if c["complete"]]
    if not args.smoke_preview and len(cases) < 200:
        raise ValueError("Scientific judge validation requires at least 200 cases; --smoke-preview is engineering only")
    grouped = defaultdict(list)
    for case in cases:
        grouped[(case["language"], case["model_id"], case["fact"].category)].append(case)
    rng = random.Random(config["seed"])
    for values in grouped.values():
        rng.shuffle(values)
    sampled = []
    while grouped and len(sampled) < min(200, len(cases)):
        for key in sorted(list(grouped)):
            sampled.append(grouped[key].pop())
            if not grouped[key]:
                del grouped[key]
            if len(sampled) == min(200, len(cases)):
                break
    rows = []
    for case in sampled:
        rows.append(dict(case_id=case["case_id"], fact_id=case["fact_id"], language=case["language"],
                         model_id=case["model_id"], category=case["fact"].category, question=case["question"],
                         **{f"answer_{i+1}": s["response_text"] for i, s in enumerate(case["samples"])},
                         human_groups_json="", reviewer="", review_notes=""))
    if not rows:
        raise ValueError("No complete cases to review")
    path = project_path("data/labels") / args.experiment_id / "semantic_review_queue.csv"
    if not args.dry_run:
        if path.exists():
            raise ValueError("Review queue already exists; refusing to overwrite possible human work")
        write_rows(path, rows, list(rows[0]))
        write_json(path.with_suffix(".metadata.json"), dict(seed=config["seed"], cases=len(rows),
                   engineering_only=args.smoke_preview, blinded_to_machine_groups=True))
    return dict(cases=len(rows), path=str(path), engineering_only=args.smoke_preview)


if __name__ == "__main__":
    p = parser("Prepare stratified human semantic annotation, blinded to the judge")
    p.add_argument("--smoke-preview", action="store_true", help="Allow fewer than 200 cases for engineering inspection only")
    main(run, p)

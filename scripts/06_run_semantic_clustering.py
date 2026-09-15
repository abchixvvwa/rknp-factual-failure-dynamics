import json
import os

import pandas as pd

from _common import main, parser
from src.generation.store import Store
from src.groq.budget import Budget
from src.groq.client import Client
from src.groq.models import snapshot, require_models
from src.semantics.judge import judge_case_joint, JUDGE_VERSION, JUDGE_TRUNCATION_RETRY_CAP
from src.utils.cases import load_cases
from src.utils.hashing import stable_hash
from src.utils.io import project_path, write_json


def fact_round_robin(cases):
    """Cover every fact early without changing the frozen semantic inputs."""
    seen = {}
    ranked = []
    for case in cases:
        rank = seen.get(case["fact_id"], 0)
        seen[case["fact_id"]] = rank + 1
        ranked.append((rank, case["fact_id"], case["language"], case["model_id"], case))
    return [item[-1] for item in sorted(ranked, key=lambda item: item[:-1])]


def run(args, config):
    cases = [case for case in load_cases(config, args.experiment_id) if case["complete"]]
    if args.limit:
        ids = sorted({c["fact_id"] for c in cases})[:args.limit]
        cases = [c for c in cases if c["fact_id"] in ids]
    if not cases:
        raise ValueError("No complete 1+5 cases to cluster")
    if not 0 <= args.shard_index < args.shard_count:
        raise ValueError("--shard-index must be between 0 and --shard-count - 1")
    if args.dry_run:
        return dict(dry_run=True, cases=len(cases), max_judge_requests=len(cases),
                    note="All k=2..5 prefixes and target support are returned in one versioned request per case")
    if config["groq"].get("free_plan_confirmed") is not True:
        raise RuntimeError("Free Plan must be confirmed before semantic inference")
    folder = project_path("artifacts/semantic_judgments") / args.experiment_id / JUDGE_VERSION
    folder.mkdir(parents=True, exist_ok=True)
    binding = dict(judge_version=JUDGE_VERSION, judge=config["models"]["semantic_judge"],
                   judge_parameters=config["generation"]["semantic_judge"],
                   model_parameters=config["generation"].get("model_parameters", {}),
                   cases=[dict(case_id=c["case_id"], target=c["target"]["response_sha256"],
                               samples=[r["response_sha256"] for r in c["samples"]]) for c in cases])
    manifest = folder / "manifest.json"
    if manifest.exists() and json.loads(manifest.read_text(encoding="utf-8"))["input_hash"] != stable_hash(binding):
        raise ValueError("Semantic inputs changed; use a new experiment/configuration instead of overwriting judgments")
    write_json(manifest, dict(input_hash=stable_hash(binding), inputs=binding,
                             execution_policy=dict(truncation_retry_cap=JUDGE_TRUNCATION_RETRY_CAP)))
    cases = fact_round_robin(cases)
    cases = [case for index, case in enumerate(cases) if index % args.shard_count == args.shard_index]
    store, client = Store(project_path(config["paths"]["ledger"])), Client(config["groq"])
    log = project_path(config["paths"]["logs"]) / f"{args.experiment_id}_semantics.jsonl"
    completed = 0
    try:
        with store.writer_lock():
            _, models = snapshot(client, config["paths"]["snapshots"])
            require_models(models, [config["models"]["semantic_judge"]["id"]])
            for case in cases:
                output = folder / f"{case['case_id']}.json"
                if output.exists():
                    continue
                prefixes = judge_case_joint(store, client, config, args.experiment_id, case, log)
                write_json(output, dict(case_id=case["case_id"], prefixes=prefixes))
                completed += 1
    finally:
        audits = []
        for file in folder.glob("*.json"):
            if file.name in ("budget.json", "manifest.json"):
                continue
            value = json.loads(file.read_text(encoding="utf-8"))
            for prefix in value.get("prefixes", []):
                audits.extend(a for a in (prefix["audit"], prefix["support_audit"]) if a)
        if audits:
            temporary = folder / f"judgments.{os.getpid()}.tmp.parquet"
            pd.DataFrame(audits).to_parquet(temporary, index=False)
            os.replace(temporary, folder / "judgments.parquet")
        write_json(folder / "budget.json", Budget(store, config["groq"]).summary())
        export_path = config["paths"].get("semantic_export", config["paths"]["generations"])
        store.export(project_path(export_path))
        client.close()
        store.close()
    return dict(complete_cases=len(cases), clustered=completed)


if __name__ == "__main__":
    argument_parser = parser("Cluster each visible prefix and match the target without ground truth")
    argument_parser.add_argument("--shard-count", type=int, default=1)
    argument_parser.add_argument("--shard-index", type=int, default=0)
    main(run, argument_parser)

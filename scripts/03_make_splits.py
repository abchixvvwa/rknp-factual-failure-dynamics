from _common import main, parser
from src.benchmark.split import make_splits, save_splits
from src.benchmark.validate import read_benchmark
from src.utils.hashing import file_hash, stable_hash
from src.utils.io import project_path, write_json


def run(args, config):
    source = project_path(config["paths"]["benchmark"])
    facts = read_benchmark(source)
    if args.limit and args.limit < len(facts):
        raise ValueError("Do not split a partial benchmark; create a separate benchmark/config for smoke")
    rows = make_splits(facts, config["splits"], config["seed"])
    path = project_path(config["paths"]["splits"])
    if not args.dry_run:
        if project_path("experiments/main/FROZEN_CONFIG.yaml").exists():
            raise RuntimeError("Main protocol is frozen; use a versioned benchmark and a new experiment")
        if path.exists():
            import csv
            with path.open(encoding="utf-8", newline="") as stream:
                existing = list(csv.DictReader(stream))
            if existing != rows:
                raise RuntimeError("Existing splits differ; version the benchmark and split path explicitly")
        save_splits(path, rows)
        write_json(path.with_suffix(".metadata.json"), dict(benchmark_sha256=file_hash(source),
                   split_sha256=file_hash(path), seed=config["seed"], proportions=config["splits"]))
    return dict(dry_run=args.dry_run, facts=len(rows), assignments_hash=stable_hash(rows),
                counts={name: sum(r["split"] == name for r in rows) for name in config["splits"]})


if __name__ == "__main__":
    main(run, parser("Create deterministic category-balanced fact-level splits"))

import json
from collections import defaultdict

import pandas as pd

from src.benchmark.validate import read_benchmark
from src.utils.hashing import file_hash, stable_hash
from src.utils.io import project_path


def load_cases(config, experiment_id):
    path = project_path(config["paths"]["benchmark"])
    facts = {f.fact_id: f for f in read_benchmark(path)}
    metadata = json.loads((project_path("experiments/pilot") / experiment_id / "metadata.json").read_text(encoding="utf-8"))
    if metadata["benchmark_hash"] != file_hash(path):
        raise ValueError("Benchmark hash differs from the generation run")
    frame = pd.read_parquet(project_path(config["paths"]["generations"]))
    frame = frame[frame.experiment_id.eq(experiment_id) & frame.generation_type.isin(["target", "sample"])]
    grouped = defaultdict(list)
    for row in frame.to_dict("records"):
        grouped[(row["fact_id"], row["language"], row["model_id"])].append(row)
    cases = []
    for (fact_id, language, model), rows in sorted(grouped.items()):
        targets = [r for r in rows if r["generation_type"] == "target"]
        samples = sorted([r for r in rows if r["generation_type"] == "sample"], key=lambda r: r["sample_index"])
        complete = (len(targets) == 1 and len(samples) == 5 and
                    [r["sample_index"] for r in samples] == [1, 2, 3, 4, 5] and all(r["valid_response"] for r in rows))
        fact = facts[fact_id]
        cases.append(dict(case_id=stable_hash([experiment_id, fact_id, language, model]),
                          fact=fact, fact_id=fact_id, language=language, model_id=model,
                          question=getattr(fact, f"question_{language}"), target=targets[0] if len(targets) == 1 else None,
                          samples=samples, complete=complete))
    return cases

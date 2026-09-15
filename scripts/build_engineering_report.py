import json
import re
from collections import Counter

import pandas as pd

from _common import main, parser
from src.generation.store import Store
from src.utils.cases import load_cases
from src.utils.hashing import file_hash
from src.utils.io import project_path, atomic_write, write_json


def run(args, config):
    cases = load_cases(config, args.experiment_id)
    frame = pd.read_parquet(project_path(config["paths"]["generations"]))
    frame = frame[frame.experiment_id.eq(args.experiment_id) & frame.generation_type.isin(["target", "sample"])]
    invalid = frame[~frame.valid_response]
    summary_path = project_path("experiments/pilot") / args.experiment_id / "last_run.json"
    planned = json.loads(summary_path.read_text(encoding="utf-8"))["planned"] if summary_path.exists() else None
    refusal = re.compile(r"\bi (?:do not|don't) know\b|\bне знаю\b|\bбілмеймін\b", re.IGNORECASE)
    counts = frame.groupby("model_id").agg(requests=("request_id", "size"), input_tokens=("prompt_tokens", "sum"),
                                         output_tokens=("completion_tokens", "sum")).reset_index().to_dict("records")
    failures = [dict(case_id=c["case_id"], fact_id=c["fact_id"], language=c["language"], model_id=c["model_id"],
                     missing_target=c["target"] is None,
                     valid_samples=sum(bool(r["valid_response"]) for r in c["samples"])) for c in cases if not c["complete"]]
    report = dict(experiment_id=args.experiment_id, engineering_only=True,
                  benchmark_sha256=file_hash(project_path(config["paths"]["benchmark"])),
                  requests=len(frame), duplicate_request_keys=int(frame.request_id.duplicated().sum()),
                  expected_requests=planned, expected_cases=planned//6 if planned is not None else None,
                  empty_responses=int(frame.response_text.fillna("").str.strip().eq("").sum()),
                  refusal_marker_responses=sum(bool(refusal.search(t)) for t in frame.response_text.fillna("")),
                  repeated_sample_texts=sum(len(c["samples"])-len({s["response_text"] for s in c["samples"]}) for c in cases),
                  fingerprints_by_model={str(m): sorted(set(g.system_fingerprint.dropna().astype(str))) for m, g in frame.groupby("model_id")},
                  observed_cases=len(cases), complete_cases=sum(c["complete"] for c in cases),
                  invalid_responses=len(invalid), exclusions=failures, by_model=counts,
                  invalid_by_language=dict(Counter(invalid.language)), invalid_by_model=dict(Counter(invalid.model_id)),
                  finish_reasons=dict(Counter(frame.finish_reason)),
                  interpretation="Engineering feasibility evidence, not a scientific pilot and not evidence for predictive hypotheses")
    if not args.dry_run:
        folder = project_path("results/reports")
        write_json(folder / f"{args.experiment_id}_engineering.json", report)
        text = (f"# Технический отчёт: {args.experiment_id}\n\n"
                f"Это engineering smoke, а не научный pilot. Метрики классификатора не рассчитывались.\n\n"
                f"Сохранено ответов: {len(frame)}. Полных случаев: {report['complete_cases']} из {len(cases)}. "
                f"Непригодных ответов: {len(invalid)}. Повторяющихся request keys: {report['duplicate_request_keys']}.\n\n"
                f"SHA-256 benchmark: `{report['benchmark_sha256']}`.\n\n"
                "## Реальный расход Groq\n\n| Model | Requests | Input tokens | Output tokens |\n|---|---:|---:|---:|\n" +
                "".join(f"| {r['model_id']} | {r['requests']} | {r['input_tokens']} | {r['output_tokens']} |\n" for r in counts) +
                "\n## Неполные случаи\n\n" + ("\n".join(f"- {r['fact_id']}, {r['language']}, {r['model_id']}: {r['valid_samples']}/5 пригодных samples." for r in failures) or "Нет.") +
                "\n\nСбои сохранены и исключены из fixed-five анализа; они не подменены фактическими ошибками. "
                "Потеря случаев может зависеть от языка и модели и должна учитываться в ограничениях исследования.\n")
        atomic_write(folder / f"{args.experiment_id}_engineering.md", text)
    return report


if __name__ == "__main__":
    main(run, parser("Report actual smoke generation counts and explicit exceptions"))

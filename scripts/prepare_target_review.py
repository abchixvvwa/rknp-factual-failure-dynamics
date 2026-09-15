"""Snapshot unresolved target labels into readable, immutable review batches."""
import csv
import json

from _common import main, parser
from src.benchmark.validate import read_benchmark
from src.generation.run import validate_id
from src.labeling.manual_queue import write_rows
from src.utils.hashing import file_hash, stable_hash
from src.utils.io import atomic_write, project_path, write_json


def run(args, config):
    validate_id(args.experiment_id)
    if args.limit:
        raise ValueError("Limit facts when building labels, before preparing their review snapshot")
    source = project_path(f"data/labels/{args.experiment_id}/manual_review_queue.csv")
    with source.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    invalid = [row for row in rows if row["auto_reason"] == "Invalid/truncated target"]
    rows = [row for row in rows if row["auto_reason"] != "Invalid/truncated target"]
    digest = stable_hash([(row["request_id"], row["response_sha256"]) for row in rows])
    folder = project_path(f"data/reviews/{args.experiment_id}/targets_{digest[:12]}")
    result = dict(experiment_id=args.experiment_id, unresolved_reviewable=len(rows),
                  invalid_targets_excluded=len(invalid), source_queue_sha256=file_hash(source), queue_sha256=digest,
                  folder=str(folder), batches=(len(rows) + 49) // 50, human_review_received=False)
    if args.dry_run:
        return result
    if folder.exists():
        raise ValueError("Review snapshot already exists; preserve its numbering and any user edits")
    facts = {f.fact_id: f for f in read_benchmark(project_path(config["paths"]["benchmark"]))}
    folder.mkdir(parents=True)
    write_rows(folder / "queue.csv", rows, list(rows[0]))
    for start in range(0, len(rows), 50):
        lines = [f"# Проверка ответов моделей: {args.experiment_id}", "",
                 f"Пакет {start // 50 + 1}. Номера {start + 1}–{min(start + 50, len(rows))}. "
                 "Это часть пилота, по уже полученным ответам; сбор остальных продолжается.", "",
                 "Оцените весь ответ: 1 — фактически верен, 0 — фактически неверен. "
                 "Если случай неоднозначен или ответ оборван, оставьте пояснение вместо догадки. "
                 "Для ложной предпосылки ответ должен явно её отвергать. "
                 "Можно прислать номера и оценки в чат, указав название пакета.", "",
                 "Проверка эталонных фактов ранее не означает проверки этих ответов моделей.", ""]
        for number, row in enumerate(rows[start:start + 50], start + 1):
            fact = facts[row["fact_id"]]
            lines += [f"## {number}. {row['fact_id']} / {row['language']} / {row['model_id']}", "",
                      f"Вопрос: {row['question']}", "", f"Эталон: {row['canonical_answer']}", "",
                      "Варианты: " + "; ".join(json.loads(row['acceptable_aliases'])), "",
                      f"[Источник]({fact.source_url})", "", "Ответ модели:", ""]
            lines += ["> " + line for line in row['target_response'].splitlines()]
            lines += ["", f"Причина проверки: {row['auto_reason']}", "", "Оценка / пояснение: ___", "",
                      f"request_id: `{row['request_id']}`", f"response_sha256: `{row['response_sha256']}`", ""]
        atomic_write(folder / f"batch_{start // 50 + 1:02}.md", "\n".join(lines))
    write_json(folder / "manifest.json", result | dict(numbered_requests=[
        dict(number=i, request_id=r['request_id'], response_sha256=r['response_sha256'])
        for i, r in enumerate(rows, 1)]))
    return result


if __name__ == "__main__":
    main(run, parser("Prepare immutable numbered human-review batches from unresolved target labels"))

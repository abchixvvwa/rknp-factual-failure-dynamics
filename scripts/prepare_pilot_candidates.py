"""Expand curated source records into reviewable CSV; never attest human review."""
import csv
import io
import json
from collections import Counter

from _common import main, parser
from src.benchmark.schema import Fact
from src.utils.hashing import file_hash
from src.utils.io import atomic_write, project_path, write_json


def run(args, config):
    seed = project_path("data/benchmark/pilot_candidates_v1.seed.json")
    entries = json.loads(seed.read_text(encoding="utf-8"))
    if args.limit:
        entries = entries[:args.limit]
    facts = []
    for index, entry in enumerate(entries, 1):
        url, title, publisher = entry["source"]
        facts.append(Fact(fact_id=f"pilot_{index:03}", category=entry["category"], difficulty="unrated",
                          question_type=entry["type"], question_en=entry["q"][0], question_ru=entry["q"][1],
                          question_kk=entry["q"][2], canonical_answer=entry["answer"],
                          acceptable_aliases_json=json.dumps(entry["aliases"], ensure_ascii=False),
                          false_premise=entry["type"] == "false_premise", source_url=url,
                          source_title=title, source_publisher=publisher, source_accessed_date="2026-09-11",
                          verified_by_human=False, notes="Pilot candidate only. EN/RU/KK, sources and aliases await human review. " + entry.get("notes", "")))
    destination = project_path("data/benchmark/pilot_candidates_v1.csv")
    report_path = project_path("results/reports/pilot_candidates_v1_review.md")
    counts = Counter(f.category for f in facts)
    result = dict(facts=len(facts), target=100, remaining=max(0, 100-len(facts)), categories=dict(counts),
                  verified_by_human=0, seed_sha256=file_hash(seed), inference_started=False,
                  status="Incomplete candidate batch; not the scientific pilot benchmark")
    if not args.dry_run:
        if destination.exists() or report_path.exists():
            raise ValueError("Candidate review files already exist; refusing to overwrite human edits")
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, fieldnames=list(Fact.model_fields))
        writer.writeheader()
        writer.writerows(f.csv_row() for f in facts)
        atomic_write(destination, stream.getvalue())
        lines = ["# Проверка кандидатов для pilot", "", f"Подготовлено {len(facts)} из 100 новых фактов. Это неполная первая партия.", "",
                 "Все строки пока ожидают вашей проверки. Для каждой проверьте ответ, источник, допустимые варианты и равнозначность EN/RU/KK.",
                 "Напишите номера проверенных строк и исправления. Для вопросов с ложной предпосылкой правильный ответ должен отвергать её.", "",
                 "Сложность пока не оценена. До полного набора нужно расширить тематическое разнообразие; текущая история сосредоточена на Apollo, культура — на Нобелевской премии.", ""]
        for fact in facts:
            lines += [f"## {fact.fact_id} — {fact.category}", "", f"EN: {fact.question_en}", "", f"RU: {fact.question_ru}", "",
                      f"KK: {fact.question_kk}", "", f"Ответ: **{fact.canonical_answer}**", "",
                      "Варианты: " + "; ".join(json.loads(fact.acceptable_aliases_json)), "",
                      f"[Источник: {fact.source_title}]({fact.source_url})", "", f"Примечание: {fact.notes}", "", "Проверка: ___", ""]
        atomic_write(report_path, "\n".join(lines))
        result["csv_sha256"] = file_hash(destination)
        write_json(destination.with_suffix(".metadata.json"), result)
    return result


if __name__ == "__main__":
    main(run, parser("Prepare sourced pilot candidates for human review"))

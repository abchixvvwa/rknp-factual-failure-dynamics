"""Assemble the 24 reviewed facts and 76 sourced candidates without changing either."""
import csv
import io
import json
from collections import Counter

from _common import main, parser
from src.benchmark.schema import Fact
from src.benchmark.split import make_splits
from src.benchmark.validate import read_benchmark
from src.utils.hashing import file_hash
from src.utils.io import atomic_write, project_path, write_json


def csv_text(facts):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(Fact.model_fields), lineterminator="\n")
    writer.writeheader()
    writer.writerows(fact.csv_row() for fact in facts)
    return stream.getvalue()


def run(args, config):
    if args.limit:
        raise ValueError("Assemble the complete pilot, not a partial --limit subset")
    original = project_path("data/benchmark/pilot_verified_v1.csv")
    seed_path = project_path("data/benchmark/pilot_remaining_v1.seed.json")
    reviewed = read_benchmark(original, main=True)
    seed = json.loads(seed_path.read_text(encoding="utf-8"))
    if [row[0] for row in seed["facts"]] != list(range(25, 101)) or len(reviewed) != 24:
        raise ValueError("Expected exactly reviewed pilot_001–024 and candidates pilot_025–100")
    page_sources = set("paris louisiana vote canyon serengeti galapagos petra sagarmatha komodo socotra thingvellir jeju rapanui hydrogen carbon oxygen iron gold sodium memory yasawi tanbaly saryarka flag emblem anthem landlocked".split())
    pending = []
    for number, category, kind, en, ru, kk, answer, aliases, key in seed["facts"]:
        url, title, publisher = seed["sources"][key]
        evidence = "primary-source page" if key in page_sources else "official-source indexed extract"
        notes = f"Agent checked {evidence} on 2026-09-11. Human review of answer, source, EN/RU/KK and aliases pending; difficulty unrated."
        if kind == "false_premise":
            notes += " Correct answer must reject the presupposed event/entity; an invented name or year is incorrect."
        pending.append(Fact(fact_id=f"pilot_{number:03}", category=category, difficulty="unrated", question_type=kind,
                            question_en=en, question_ru=ru, question_kk=kk, canonical_answer=answer,
                            acceptable_aliases_json=json.dumps(aliases, ensure_ascii=False), false_premise=kind == "false_premise",
                            source_url=url, source_title=title, source_publisher=publisher, source_accessed_date="2026-09-11",
                            notes=notes, verified_by_human=False))
    combined = reviewed + pending
    if [f.fact_id for f in combined] != [f"pilot_{i:03}" for i in range(1, 101)]:
        raise ValueError("Unexpected or overlapping fact IDs")
    for language in ("en", "ru", "kk"):
        if len({getattr(f, f"question_{language}").casefold().strip() for f in combined}) != 100:
            raise ValueError(f"Duplicate question in {language}")
    counts = dict(Counter(f.category for f in combined))
    expected = dict.fromkeys(("history", "geography", "science", "culture", "kazakhstan"), 16)
    expected["adversarial_false_premise"] = 20
    if counts != expected:
        raise ValueError("Pilot category counts differ from the supplied plan")
    preview = make_splits(combined, config["splits"], config["seed"])
    result = dict(facts=100, language_questions=300, human_verified=24, pending_human_review=76, categories=counts,
                  question_types=dict(Counter(f.question_type for f in combined)),
                  split_preview=dict(Counter(row["split"] for row in preview)), splits_saved=False,
                  original_verified_sha256=file_hash(original), seed_sha256=file_hash(seed_path),
                  inference_started=False, frozen=False,
                  limitations=["Convenience sample; difficulty not yet rated.",
                               "Within-category concentrations: visual art, atomic numbers, UNESCO locations, Nobel awards.",
                               "Related topics are not statistically independent merely because fact IDs differ.",
                               "New source evidence includes indexed extracts, not uniformly successful direct fetches.",
                               "All pilot facts are development data and must stay out of a later untouched main test."])
    if args.dry_run:
        return result
    remaining_path = project_path("data/benchmark/pilot_remaining_v1.csv")
    combined_path = project_path("data/benchmark/pilot100_candidates_v1.csv")
    report_path = project_path("results/reports/pilot_remaining_v1_review.md")
    config_path = project_path("configs/pilot100_candidate_v1.json")
    metadata_path = combined_path.with_suffix(".metadata.json")
    for path in (remaining_path, combined_path, report_path, config_path, metadata_path):
        if path.exists():
            raise ValueError(f"Refusing to overwrite existing review/preparation file: {path.name}")
    atomic_write(remaining_path, csv_text(pending))
    atomic_write(combined_path, csv_text(combined))
    lines = ["# Pilot: проверка оставшихся 76 фактов", "",
             "Первые 24 факта уже проверены вами и сохранены без изменений. Здесь только pilot_025–pilot_100.", "",
             "Проверьте правильный ответ, источник, допустимые варианты и одинаковый смысл EN/RU/KK. Можно присылать проверенные диапазоны и исправления прямо в чат.", "",
             "Все 76 строк пока имеют verified_by_human=false. Ссылки ведут на первичные источники; для части использован официальный поисковый фрагмент, что указано в примечании.", "",
             "Полный набор: 100 фактов, 300 языковых формулировок; по 16 фактов в пяти обычных категориях и 20 с ложной предпосылкой. Это подготовка pilot, не замороженный main benchmark.", ""]
    for fact in pending:
        lines += [f"## {fact.fact_id} — {fact.category}", "", f"EN: {fact.question_en}", "", f"RU: {fact.question_ru}", "",
                  f"KK: {fact.question_kk}", "", f"Ответ: **{fact.canonical_answer}**", "",
                  "Допустимые варианты: " + ("; ".join(json.loads(fact.acceptable_aliases_json)) or "Точный числовой ответ"), "",
                  f"[Источник: {fact.source_title}]({fact.source_url})", "", f"Примечание: {fact.notes}", "", "Проверка / исправления: ___", ""]
    atomic_write(report_path, "\n".join(lines))
    config["paths"]["benchmark"] = str(combined_path.relative_to(project_path("."))).replace("\\", "/")
    config["paths"]["splits"] = "data/processed/splits_pilot100_v1.csv"
    config["pilot"]["require_human_verified"] = True
    write_json(config_path, config)
    result.update(combined_sha256=file_hash(combined_path), remaining_sha256=file_hash(remaining_path),
                  review_sha256=file_hash(report_path), candidate_config_sha256=file_hash(config_path))
    write_json(metadata_path, result)
    return result


if __name__ == "__main__":
    main(run, parser("Assemble the full 100-fact candidate pilot and a 76-fact human review document"))

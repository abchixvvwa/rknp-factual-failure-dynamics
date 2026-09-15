import json
import sqlite3
from itertools import combinations

from _common import main, parser
from src.semantics.judge import JUDGE_VERSION
from src.utils.io import project_path, write_json


def pair_revisions(prefixes):
    changes = 0
    for before, after in zip(prefixes, prefixes[1:]):
        left = {i: group for group, members in enumerate(before["groups"]) for i in members}
        right = {i: group for group, members in enumerate(after["groups"]) for i in members}
        changes += sum((left[a] == left[b]) != (right[a] == right[b]) for a, b in combinations(range(before["k"]), 2))
    return changes


def run(args, config):
    folder = project_path("artifacts/semantic_judgments") / args.experiment_id / JUDGE_VERSION
    cases = [json.loads(path.read_text(encoding="utf-8")) for path in folder.glob("*.json") if len(path.stem) == 64]
    revisions = [dict(case_id=c["case_id"], previous_pair_revisions=pair_revisions(c["prefixes"])) for c in cases]
    db = sqlite3.connect(project_path(config["paths"]["ledger"]).as_uri() + "?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    try:
        rows = db.execute("""SELECT a.state,a.status,a.record FROM attempts a JOIN requests r ON a.request_key=r.key
            WHERE json_extract(r.spec,'$.experiment_id')=? AND json_extract(r.spec,'$.prompt_version')=?""",
                                (args.experiment_id, JUDGE_VERSION)).fetchall()
        valid, malformed, failed = 0, 0, 0
        for row in rows:
            if row["state"] != "success":
                failed += 1
                continue
            record = json.loads(row["record"])
            try:
                parsed = json.loads(record["response_text"])
                schema = record["response_format"]["json_schema"]["schema"]
                assert record["valid_response"] and type(parsed["uncertain"]) is bool
                if "assignments" in schema["properties"]:
                    letters = schema["properties"]["assignments"]["required"]
                    assert set(parsed["assignments"]) == set(letters)
                    assert all(type(v) is int and 0 <= v < len(letters) for v in parsed["assignments"].values())
                else:
                    assert parsed["matching_group"] is None or type(parsed["matching_group"]) is int
                    assert parsed["matching_group"] in schema["properties"]["matching_group"]["enum"]
                valid += 1
            except (ValueError, KeyError, TypeError, AssertionError):
                malformed += 1
    finally:
        db.close()
    result = dict(judge_version=JUDGE_VERSION, completed_case_files=len(cases),
                  uncertain_cases=sum(any(p["uncertain"] for p in c["prefixes"]) for c in cases),
                  valid_structured_responses=valid, invalid_structured_responses=malformed,
                  failed_api_attempts=failed, structured_success_rate=valid/(valid+malformed+failed) if rows else None,
                  cases_with_prefix_pair_revisions=sum(r["previous_pair_revisions"] > 0 for r in revisions),
                  prefix_revision_details=[r for r in revisions if r["previous_pair_revisions"]],
                  human_judge_agreement="not measured", scientific_gate="requires independent human semantic annotations")
    if not args.dry_run:
        write_json(project_path("results/reports") / f"{args.experiment_id}_semantic_quality.json", result)
    return result


if __name__ == "__main__":
    main(run, parser("Report schema validity and changes in previously judged pair relations"))

import json

from src.labeling.exact_match import exact_match
from src.labeling.numeric_match import numeric_match
from src.labeling.date_match import date_match


def automatic_label(fact, response):
    aliases = json.loads(fact.acceptable_aliases_json)
    if exact_match(response, fact.canonical_answer, aliases):
        return dict(is_factually_correct=1, label_status="auto_correct", auto_reason="Exact canonical/alias match")
    match = None
    if fact.question_type == "numeric":
        match = numeric_match(response, fact.canonical_answer)
    elif fact.question_type == "date":
        match = date_match(response, fact.canonical_answer)
    if match is not None:
        return dict(is_factually_correct=int(match), label_status="auto_correct" if match else "auto_incorrect",
                    auto_reason=f"Strict {fact.question_type} comparison")
    return dict(is_factually_correct=None, label_status="unresolved",
                auto_reason="Needs human review; non-match alone does not establish incorrectness")


def build_labels(cases, reviews=()):
    lookup = {}
    for review in reviews:
        if str(review.get("review_label", "")).strip() == "":
            continue
        if str(review["review_label"]) not in ("0", "1") or not review.get("reviewer", "").strip():
            raise ValueError("A manual label needs 0/1 and an identified reviewer")
        key = review["request_id"]
        if key in lookup:
            raise ValueError("Duplicate reviewed request_id")
        lookup[key] = review
    rows = []
    for case in cases:
        target = case["target"]
        if target is None:
            continue
        fact = case["fact"]
        label = automatic_label(fact, target["response_text"]) if target["valid_response"] else dict(
            is_factually_correct=None, label_status="unresolved", auto_reason="Invalid/truncated target")
        review = lookup.get(target["request_id"])
        if review:
            if review["response_sha256"] != target["response_sha256"]:
                raise ValueError("Stale human review: response hash mismatch")
            correct = int(review["review_label"])
            label.update(is_factually_correct=correct, label_status="manual_correct" if correct else "manual_incorrect")
        rows.append(dict(case_id=case["case_id"], request_id=target["request_id"],
                         response_sha256=target["response_sha256"], fact_id=case["fact_id"],
                         language=case["language"], model_id=case["model_id"], question=case["question"],
                         canonical_answer=fact.canonical_answer, acceptable_aliases=fact.acceptable_aliases_json,
                         target_response=target["response_text"], complete_case=case["complete"],
                         reviewer=review.get("reviewer", "") if review else "", review_notes=review.get("review_notes", "") if review else "",
                         **label))
    return rows

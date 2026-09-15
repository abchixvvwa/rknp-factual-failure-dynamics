from src.semantics.lexical import lexical_features
from src.uncertainty.static_features import static_features
from src.uncertainty.trajectories import dynamic_features

FEATURE_VERSION = "semantic_dynamics_v1"


def build_case_features(case, grouping, label, split, epsilon=0.05):
    if not case["complete"]:
        raise ValueError("Fixed-five features require one valid target and five valid samples")
    if grouping["case_id"] != case["case_id"]:
        raise ValueError("Grouping is for another case")
    if any(p["uncertain"] for p in grouping["prefixes"]):
        raise ValueError("Uncertain semantic grouping needs review before features")
    if label["request_id"] != case["target"]["request_id"] or label["response_sha256"] != case["target"]["response_sha256"]:
        raise ValueError("Label provenance mismatch")
    answers = [s["response_text"] for s in case["samples"]]
    prefixes = grouping["prefixes"]
    static = static_features(prefixes[-1]["groups"], answers, prefixes[-1]["target_group"])
    dynamic, _ = dynamic_features(prefixes, answers, epsilon)
    correct = label["is_factually_correct"]
    if correct in (None, ""):
        correct = None
    else:
        correct = int(correct)
    fact = case["fact"]
    return dict(case_id=case["case_id"], fact_id=case["fact_id"], split=split,
                language=case["language"], category=fact.category, difficulty=fact.difficulty,
                question_type=fact.question_type, target_model=case["model_id"],
                is_factually_correct=correct, error_label=1-correct if correct is not None else None,
                label_status=label["label_status"], target_request_id=case["target"]["request_id"],
                target_response_sha256=case["target"]["response_sha256"], feature_version=FEATURE_VERSION,
                **static, **lexical_features(answers), **dynamic)

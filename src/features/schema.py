import math

import numpy as np

STATIC_FEATURES = ["n_clusters", "largest_cluster_fraction", "second_largest_cluster_fraction", "consensus_margin",
                   "disagreement_rate", "semantic_entropy", "normalized_semantic_entropy", "unique_normalized_answers"]
SUPPORT_FEATURES = ["target_matches_dominant_cluster", "target_cluster_fraction", "target_supported_by_n_samples", "target_support_ratio"]
LEXICAL_FEATURES = ["mean_pairwise_token_jaccard", "mean_pairwise_rapidfuzz_ratio", "min_pairwise_rapidfuzz_ratio",
                    "lexical_diversity", "normalized_answer_unique_count"]
DYNAMIC_FEATURES = ([f"entropy_k{k}" for k in range(2, 6)] + [f"cluster_count_k{k}" for k in range(2, 6)] +
    ["entropy_slope", "entropy_auc", "entropy_last_delta", "entropy_max_delta", "entropy_variance", "cluster_births",
     "dominant_fraction_slope", "dominant_fraction_min", "dominant_fraction_final", "target_support_slope",
     "target_support_min", "target_support_final", "consensus_switch_count", "stabilization_step", "late_disagreement_flag"])
PREDICTOR_COLUMNS = STATIC_FEATURES + SUPPORT_FEATURES + LEXICAL_FEATURES + DYNAMIC_FEATURES


def validate_features(frame):
    required = ["case_id", "fact_id", "language", "target_model", "split", "is_factually_correct", "error_label", *PREDICTOR_COLUMNS]
    missing = set(required) - set(frame.columns)
    if missing:
        raise ValueError("Missing feature columns: " + ", ".join(sorted(missing)))
    if frame.case_id.duplicated().any() or frame.duplicated(["fact_id", "language", "target_model"]).any():
        raise ValueError("Duplicate feature case")
    if not frame.split.isin(["train", "validation", "test"]).all() or (frame.groupby("fact_id").split.nunique() > 1).any():
        raise ValueError("Invalid split or fact leakage")
    if not np.isfinite(frame[PREDICTOR_COLUMNS].to_numpy(dtype=float)).all():
        raise ValueError("Non-finite predictor; uncertain cases must be reported separately")
    if not frame.n_clusters.between(1, 5).all() or not frame.semantic_entropy.between(-1e-12, math.log(5)+1e-12).all():
        raise ValueError("Invalid fixed-five cluster count or entropy")
    resolved = frame.error_label.notna()
    if not frame.loc[resolved, "error_label"].isin([0, 1]).all() or not (
        frame.loc[resolved, "error_label"] == 1-frame.loc[resolved, "is_factually_correct"]).all():
        raise ValueError("Incorrect error-label orientation")
    if (frame.error_label.isna() != frame.is_factually_correct.isna()).any():
        raise ValueError("Correctness and error labels must be jointly resolved or missing")
    return frame

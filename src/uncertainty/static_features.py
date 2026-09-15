import math

from src.labeling.normalize import normalize
from src.uncertainty.entropy import entropy


def static_features(groups, answers, target_group):
    count = len(answers)
    if sorted(i for g in groups for i in g) != list(range(count)) or any(not g for g in groups):
        raise ValueError("Groups must partition exactly the visible answers")
    if target_group is not None and not 0 <= target_group < len(groups):
        raise ValueError("Target group out of range")
    sizes = sorted([len(g) for g in groups], reverse=True)
    largest, second = sizes[0]/count, sizes[1]/count if len(sizes) > 1 else 0.0
    h = entropy(sizes)
    dominant = min(range(len(groups)), key=lambda i: (-len(groups[i]), min(groups[i])))
    support = len(groups[target_group]) if target_group is not None else 0
    return dict(n_clusters=len(groups), largest_cluster_fraction=largest,
                second_largest_cluster_fraction=second, consensus_margin=largest-second,
                disagreement_rate=1-largest, semantic_entropy=h,
                normalized_semantic_entropy=h/math.log(count) if count > 1 else 0.0,
                unique_normalized_answers=len({normalize(a) for a in answers}),
                target_matches_dominant_cluster=int(target_group == dominant),
                target_cluster_fraction=support/count, target_supported_by_n_samples=support,
                target_support_ratio=support/count)

import numpy as np

from src.uncertainty.static_features import static_features


def dynamic_features(prefixes, answers, epsilon=0.05):
    if epsilon <= 0 or [p["k"] for p in prefixes] != list(range(2, len(answers)+1)):
        raise ValueError("Need each visible prefix k=2..n and positive epsilon")
    values = [static_features(p["groups"], answers[:p["k"]], p["target_group"]) for p in prefixes]
    ks = np.array([p["k"] for p in prefixes], dtype=float)
    entropies = np.array([v["semantic_entropy"] for v in values])
    normalized = [v["normalized_semantic_entropy"] for v in values]
    largest = [v["largest_cluster_fraction"] for v in values]
    support = [v["target_support_ratio"] for v in values]
    counts = [v["n_clusters"] for v in values]
    dominants = [min(p["groups"], key=lambda g: (-len(g), min(g)))[0] for p in prefixes]
    def slope(y):
        return float(np.polyfit(ks, y, 1)[0]) if len(ks) > 1 else 0.0
    changes = np.diff(entropies)
    stable = len(answers)
    for index, k in enumerate(ks):
        if all(d == dominants[index] for d in dominants[index:]) and all(
            abs(normalized[j+1]-normalized[j]) < epsilon for j in range(index, len(ks)-1)):
            stable = int(k)
            break
    result = {f"entropy_k{int(k)}": float(h) for k, h in zip(ks, entropies)}
    result.update({f"cluster_count_k{int(k)}": n for k, n in zip(ks, counts)})
    result.update(entropy_slope=slope(entropies), entropy_auc=float(np.trapezoid(entropies, ks)),
                  entropy_last_delta=float(changes[-1]) if len(changes) else 0.0,
                  entropy_max_delta=float(max(changes)) if len(changes) else 0.0,
                  entropy_variance=float(np.var(entropies)),
                  cluster_births=sum(max(0, b-a) for a, b in zip(counts, counts[1:])),
                  dominant_fraction_slope=slope(largest), dominant_fraction_min=min(largest),
                  dominant_fraction_final=largest[-1], target_support_slope=slope(support),
                  target_support_min=min(support), target_support_final=support[-1],
                  consensus_switch_count=sum(a != b for a, b in zip(dominants, dominants[1:])),
                  stabilization_step=stable, late_disagreement_flag=int(counts[-1] > counts[-2]) if len(counts)>1 else 0)
    return result, values

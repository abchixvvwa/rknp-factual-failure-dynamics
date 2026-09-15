from itertools import combinations

from sklearn.metrics import adjusted_rand_score


def agreement(predicted, human):
    if len(predicted) != len(human) or len(human) < 2:
        raise ValueError("Aligned human and judge labels are required")
    pairs = list(combinations(range(len(human)), 2))
    pairwise = sum((predicted[a] == predicted[b]) == (human[a] == human[b]) for a, b in pairs)/len(pairs)
    return dict(adjusted_rand_index=float(adjusted_rand_score(human, predicted)),
                pairwise_agreement=pairwise, exact_cluster_match=pairwise == 1.0)

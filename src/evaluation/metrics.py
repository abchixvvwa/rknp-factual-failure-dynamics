import numpy as np
from sklearn.metrics import (accuracy_score, average_precision_score, brier_score_loss,
                             f1_score, precision_score, recall_score, roc_auc_score)


def metrics(y, probability, threshold=0.5, bins=10):
    y, probability = np.asarray(y), np.asarray(probability, dtype=float)
    if y.ndim != 1 or y.shape != probability.shape or not len(y):
        raise ValueError("Aligned, nonempty one-dimensional labels and probabilities required")
    if not set(y.tolist()) <= {0, 1} or not np.isfinite(probability).all() or np.any((probability < 0) | (probability > 1)):
        raise ValueError("Labels must be binary and probabilities finite in [0,1]")
    if not 0 <= threshold <= 1 or type(bins) is not int or bins <= 0:
        raise ValueError("Invalid threshold or calibration bins")
    prediction = probability >= threshold
    groups = np.minimum((probability*bins).astype(int), bins-1)
    ece = sum(np.mean(groups == b) * abs(float(y[groups == b].mean()) - float(probability[groups == b].mean()))
              for b in range(bins) if np.any(groups == b))
    both = len(set(y.tolist())) == 2
    return dict(n=len(y), positives=int(y.sum()),
                auroc=float(roc_auc_score(y, probability)) if both else None,
                auprc=float(average_precision_score(y, probability)) if both else None,
                f1=float(f1_score(y, prediction, zero_division=0)),
                precision=float(precision_score(y, prediction, zero_division=0)),
                recall=float(recall_score(y, prediction, zero_division=0)),
                accuracy=float(accuracy_score(y, prediction)), brier=float(brier_score_loss(y, probability)), ece=float(ece))


def select_threshold(y_validation, probabilities, criterion="max_f1"):
    candidates = np.unique(np.r_[0.0, probabilities, 1.0])
    results = [(float(t), metrics(y_validation, probabilities, float(t))) for t in candidates]
    if criterion == "max_f1":
        return max(results, key=lambda item: (item[1]["f1"], item[1]["recall"], -item[0]))[0]
    if criterion == "recall_90":
        eligible = [r for r in results if r[1]["recall"] >= .90]
        if not eligible:
            raise ValueError("No threshold meets the validation recall requirement")
        return max(eligible, key=lambda item: (item[1]["precision"], item[1]["recall"], -item[0]))[0]
    raise ValueError("Unknown threshold selection criterion")

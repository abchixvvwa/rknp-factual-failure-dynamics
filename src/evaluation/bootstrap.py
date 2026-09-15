import numpy as np

from src.evaluation.metrics import metrics


def bootstrap(y, scores, fact_ids, resamples=1000, confidence=.95, seed=42, paired_scores=None, threshold=.5):
    y, scores, fact_ids = np.asarray(y), np.asarray(scores), np.asarray(fact_ids)
    if y.shape != scores.shape or y.shape != fact_ids.shape or y.ndim != 1 or not len(y):
        raise ValueError("Labels, scores and fact IDs must be aligned")
    if resamples < 1 or not 0 < confidence < 1:
        raise ValueError("Invalid bootstrap configuration")
    metrics(y, scores, threshold)  # Validate the full arrays, including otherwise unsampled rows.
    if paired_scores is not None:
        paired_scores = np.asarray(paired_scores)
        metrics(y, paired_scores, threshold)
    unique = np.unique(fact_ids)
    indexes = [np.flatnonzero(fact_ids == fact) for fact in unique]
    rng, distributions = np.random.default_rng(seed), {"auroc": [], "auprc": []}
    paired = {"delta_auroc": [], "delta_auprc": []}
    for _ in range(resamples):
        # Select whole facts with replacement, retaining every language/model row and multiplicity.
        selection = np.concatenate([indexes[i] for i in rng.integers(len(unique), size=len(unique))])
        value = metrics(y[selection], scores[selection], threshold)
        other = metrics(y[selection], paired_scores[selection], threshold) if paired_scores is not None else None
        for name in distributions:
            if value[name] is not None:
                distributions[name].append(value[name])
                if other is not None:
                    paired[f"delta_{name}"].append(value[name] - other[name])
    alpha = (1-confidence)/2
    def interval(values):
        return dict(lower=float(np.quantile(values, alpha)) if values else None,
                    upper=float(np.quantile(values, 1-alpha)) if values else None,
                    valid_resamples=len(values), skipped_single_class=resamples-len(values))
    result = {name: interval(values) for name, values in distributions.items()}
    if paired_scores is not None:
        result.update({name: interval(values) for name, values in paired.items()})
    return dict(unit="fact_id", confidence=confidence, requested_resamples=resamples, intervals=result)

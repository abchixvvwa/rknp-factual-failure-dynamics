import numpy as np
from sklearn.base import clone
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedGroupKFold


def log_odds(probability):
    p = np.clip(np.asarray(probability, dtype=float), 1e-6, 1-1e-6)
    return np.log(p/(1-p)).reshape(-1, 1)


def fit_calibrators(estimator, X, y, fact_ids, seed=42):
    """Fit on train-only out-of-fold scores, keeping every fact in one fold."""
    y, fact_ids = np.asarray(y), np.asarray(fact_ids)
    for count in range(min(5, len(set(fact_ids))), 1, -1):
        folds = list(StratifiedGroupKFold(count, shuffle=True, random_state=seed).split(X, y, fact_ids))
        if all(len(set(y[train])) == 2 for train, _ in folds):
            break
    else:
        raise ValueError("Too few independently labeled train facts for grouped calibration")
    scores = np.full(len(y), np.nan)
    assignments = np.full(len(y), -1)
    for fold, (train, held_out) in enumerate(folds):
        fitted = clone(estimator).fit(X.iloc[train], y[train])
        scores[held_out] = fitted.predict_proba(X.iloc[held_out])[:, 1]
        assignments[held_out] = fold
    sigmoid = LogisticRegression(C=1e6, max_iter=2000, random_state=seed).fit(log_odds(scores), y)
    isotonic = IsotonicRegression(out_of_bounds="clip").fit(scores, y)
    return {"raw": None, "sigmoid": sigmoid, "isotonic": isotonic}, assignments


def calibrated_probability(calibrator, method, raw):
    if method == "raw":
        return np.asarray(raw)
    if method == "sigmoid":
        return calibrator.predict_proba(log_odds(raw))[:, 1]
    if method == "isotonic":
        return calibrator.predict(raw)
    raise ValueError("Unknown calibration method")

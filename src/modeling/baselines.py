import math

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from src.features.schema import DYNAMIC_FEATURES, STATIC_FEATURES, SUPPORT_FEATURES


class FixedRisk(ClassifierMixin, BaseEstimator):
    """Predeclared ranking scores; raw scores are not calibrated probabilities."""

    def __init__(self, method):
        self.method = method

    def fit(self, X, y):
        self.classes_ = np.array([0, 1])
        return self

    def predict_proba(self, X):
        if self.method == "unique":
            risk = (X.iloc[:, 0].to_numpy() - 1) / 4
        elif self.method == "lexical":
            risk = 1 - X.to_numpy().mean(axis=1)
        elif self.method == "entropy":
            risk = X.iloc[:, 0].to_numpy() / math.log(5)
        elif self.method == "support":
            risk = 1 - X.iloc[:, 0].to_numpy()
        else:
            raise ValueError("Unknown fixed risk method")
        risk = np.clip(risk, 0, 1)
        return np.column_stack([1-risk, risk])


def candidates(family, seed=42):
    logistic = lambda: make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=2000, random_state=seed))
    if family == "baselines":
        return {
            "B0_prior": (DummyClassifier(strategy="prior"), ["semantic_entropy"]),
            "B1_unique": (FixedRisk("unique"), ["unique_normalized_answers"]),
            "B2_lexical": (FixedRisk("lexical"), ["mean_pairwise_token_jaccard", "mean_pairwise_rapidfuzz_ratio"]),
            "B3_entropy": (FixedRisk("entropy"), ["semantic_entropy"]),
            "B4_static": (logistic(), STATIC_FEATURES),
            "B5_support": (FixedRisk("support"), ["target_support_ratio"]),
        }
    if family == "dynamic":
        columns = STATIC_FEATURES + SUPPORT_FEATURES + DYNAMIC_FEATURES
        return {
            "dynamic_logistic": (logistic(), columns),
            "dynamic_random_forest": (RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=seed, n_jobs=-1), columns),
            "dynamic_hist_gradient": (HistGradientBoostingClassifier(max_iter=100, max_leaf_nodes=15, l2_regularization=1.0, random_state=seed, early_stopping=False), columns),
        }
    raise ValueError("Unknown candidate family")

import numpy as np
import pytest
from sklearn.metrics import roc_auc_score, average_precision_score

from src.evaluation.metrics import metrics, select_threshold
from src.evaluation.bootstrap import bootstrap


def test_metrics_match_reference_and_degenerate_cases():
    y, p = [0, 1, 0, 1], [.1, .9, .3, .8]
    result = metrics(y, p)
    assert result["auroc"] == roc_auc_score(y, p)
    assert result["auprc"] == average_precision_score(y, p)
    assert result["f1"] == 1
    assert result["brier"] == pytest.approx(.0375)
    assert metrics([0, 0], [.1, .2])["auroc"] is None
    with pytest.raises(ValueError):
        metrics([0, 1], [0, np.nan])
    assert 0 <= select_threshold(y, p) <= 1


def test_fact_bootstrap_is_reproducible_and_paired():
    y, p, ids = [0, 0, 1, 1], [.1, .2, .8, .9], ["a", "a", "b", "b"]
    a = bootstrap(y, p, ids, resamples=50, paired_scores=p)
    b = bootstrap(y, p, ids, resamples=50, paired_scores=p)
    assert a == b
    assert a["intervals"]["delta_auroc"]["lower"] == 0
    assert a["intervals"]["auroc"]["skipped_single_class"] > 0

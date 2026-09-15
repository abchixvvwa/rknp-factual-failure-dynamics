import math
import pytest

from src.uncertainty.trajectories import dynamic_features


def test_prefix_values_and_late_disagreement():
    prefixes = [dict(k=2, groups=[[0, 1]], target_group=0),
                dict(k=3, groups=[[0, 1], [2]], target_group=0),
                dict(k=4, groups=[[0, 1, 3], [2]], target_group=0),
                dict(k=5, groups=[[0, 1, 3], [2], [4]], target_group=0)]
    features, trajectory = dynamic_features(prefixes, ["a", "a", "b", "a", "c"])
    assert features["entropy_k2"] == 0
    assert features["cluster_births"] == 2
    assert features["late_disagreement_flag"] == 1
    assert features["target_support_final"] == .6
    assert features["consensus_switch_count"] == 0
    assert trajectory[1]["semantic_entropy"] == pytest.approx(-2/3*math.log(2/3)-1/3*math.log(1/3))
    early, _ = dynamic_features(prefixes[:1], ["a", "a"])
    assert "entropy_k3" not in early
    assert early["target_support_final"] == 1


def test_constant_consensus():
    prefixes = [dict(k=k, groups=[list(range(k))], target_group=0) for k in range(2, 6)]
    f, _ = dynamic_features(prefixes, ["a"]*5)
    assert f["stabilization_step"] == 2
    assert f["entropy_auc"] == 0 and f["entropy_variance"] == 0

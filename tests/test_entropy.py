import math
import pytest

from src.uncertainty.entropy import entropy
from src.uncertainty.static_features import static_features


def test_known_entropy():
    assert entropy([5]) == 0
    assert entropy([1, 1]) == pytest.approx(math.log(2))
    assert entropy([3, 1, 1]) == pytest.approx(-.6*math.log(.6)-.4*math.log(.2))
    with pytest.raises(ValueError):
        entropy([0, 1])


def test_static_support_is_not_truth():
    f = static_features([[0, 2, 3], [1], [4]], ["wrong", "other", "wrong", "wrong", "third"], 0)
    assert f["target_support_ratio"] == .6
    assert f["consensus_margin"] == pytest.approx(.4)
    assert "is_factually_correct" not in f

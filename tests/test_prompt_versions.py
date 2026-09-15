import pytest

from src.generation.prompts import PROMPTS, VERIFIED_KK, prompt


def test_old_runs_retain_old_prompt_and_new_version_uses_reviewed_kazakh():
    assert prompt("kk", "Q", "factual_v1") == PROMPTS["kk"].format(question="Q")
    assert prompt("kk", "Q", "factual_v1_kk") == VERIFIED_KK.format(question="Q")
    assert prompt("kk", "Q", "factual_v1") != prompt("kk", "Q", "factual_v1_kk")
    for language in ("en", "ru"):
        assert prompt(language, "Q", "factual_v1") == prompt(language, "Q", "factual_v1_kk")
    with pytest.raises(ValueError, match="Unknown"):
        prompt("kk", "Q", "unregistered")

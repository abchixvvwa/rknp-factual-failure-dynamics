import importlib.util
import sys
from pathlib import Path


def load_script():
    path = Path(__file__).parents[1] / "scripts" / "06_run_semantic_clustering.py"
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location("semantic_script", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_fact_round_robin_covers_facts_before_second_case():
    cases = [dict(fact_id=fact, language=language, model_id="m")
             for fact in ("a", "b") for language in ("en", "ru", "kk")]
    ordered = load_script().fact_round_robin(cases)
    assert [case["fact_id"] for case in ordered] == ["a", "b", "a", "b", "a", "b"]

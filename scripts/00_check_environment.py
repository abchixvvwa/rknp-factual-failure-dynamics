import importlib.metadata
import os
import platform

from _common import main, parser


def run(args, config):
    packages = {}
    for name in ("groq", "pandas", "numpy", "scipy", "scikit-learn", "pyarrow", "pydantic",
                 "pyyaml", "tenacity", "tqdm", "rapidfuzz", "matplotlib", "joblib", "pytest"):
        packages[name] = importlib.metadata.version(name)
    return dict(python=platform.python_version(), packages=packages,
                groq_api_key_present=bool(os.environ.get("GROQ_API_KEY")),
                free_plan_confirmed=config["groq"]["free_plan_confirmed"], network_calls=0)


if __name__ == "__main__":
    main(run, parser("Validate local environment without API calls"))

import importlib.metadata
import platform
import subprocess

from src.utils.hashing import stable_hash, file_hash
from src.utils.io import ROOT
from src.utils.time import utc_now


def metadata(experiment_id, config, benchmark=None, splits=None, snapshot=None):
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT,
                                         stderr=subprocess.DEVNULL, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        commit = None
    versions = {}
    for name in ("groq", "pandas", "numpy", "scikit-learn", "pyarrow", "pydantic", "pyyaml"):
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = None
    return dict(experiment_id=experiment_id, git_commit=commit, python_version=platform.python_version(),
                source_hashes={str(p.relative_to(ROOT)): file_hash(p) for folder in ("src", "scripts")
                               for p in sorted((ROOT / folder).rglob("*.py"))},
                package_versions=versions, config_hash=stable_hash(config),
                benchmark_hash=file_hash(benchmark) if benchmark else None,
                split_hash=file_hash(splits) if splits and splits.exists() else None,
                model_snapshot_hash=file_hash(snapshot) if snapshot else None, timestamp=utc_now())

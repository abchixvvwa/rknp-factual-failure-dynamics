import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from src.utils.io import load_config


def parser(description, default_experiment="pilot_v1", generation=False):
    result = argparse.ArgumentParser(description=description)
    result.add_argument("--config", default=None, help="Experiment YAML, default configs/experiment.yaml")
    result.add_argument("--experiment-id", default=default_experiment)
    result.add_argument("--dry-run", action="store_true", help="No API calls or research artifacts")
    result.add_argument("--limit", type=int, help="Maximum number of facts (not requests)")
    if generation:
        result.add_argument("--model", action="append", help="Repeat for multiple enabled target model IDs")
        result.add_argument("--language", choices=["en", "ru", "kk"], action="append")
        result.add_argument("--resume", action="store_true", help="Successful requests are always skipped")
        result.add_argument("--retry-uncertain", action="store_true", help="Retry interrupted in-flight attempts after inspection")
    return result


def main(run, arg_parser):
    args = arg_parser.parse_args()
    if args.limit is not None and args.limit <= 0:
        arg_parser.error("--limit must be positive")
    try:
        value = run(args, load_config(args.config))
        print(json.dumps(value, ensure_ascii=False, indent=2))
    except KeyboardInterrupt:
        print("Stopped. Completed requests remain in the durable journal.", file=sys.stderr)
        raise SystemExit(130)
    except Exception as exc:
        # Avoid printing SDK request objects/headers or authentication data.
        from src.groq.budget import BudgetExhausted, ResumeLater
        from src.utils.logging import redact
        print(redact(f"{type(exc).__name__}: {exc}"), file=sys.stderr)
        raise SystemExit(75 if isinstance(exc, (BudgetExhausted, ResumeLater)) else 1)

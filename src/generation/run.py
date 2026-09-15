import re

from src.benchmark.validate import read_benchmark
from src.generation.prompts import prompt
from src.generation.scheduler import execute
from src.generation.store import Store
from src.groq.budget import Budget
from src.groq.client import Client
from src.groq.models import snapshot, require_models
from src.utils.hashing import file_hash
from src.utils.io import project_path, write_json
from src.utils.logging import event
from src.utils.reproducibility import metadata


def validate_id(experiment_id):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,100}", experiment_id):
        raise ValueError("Use a simple experiment ID: letters, digits, _, -, .")


def selected_models(config, requested=None):
    configured = [m["id"] for m in config["models"]["target_models"] if m["enabled"]]
    selected = requested or configured
    if not selected or set(selected) - set(configured):
        raise ValueError("Requested model must be explicitly enabled in configs/models.yaml")
    return list(dict.fromkeys(selected))


def generation_specs(facts, models, languages, config, experiment_id):
    generation = config["generation"]
    for fact in facts:
        for language in languages:
            for model in models:
                base = dict(experiment_id=experiment_id, fact_id=fact.fact_id, language=language,
                            model_id=model, prompt_version=generation["prompt_version"],
                            prompt_text=prompt(language, getattr(fact, f"question_{language}"), generation["prompt_version"]))
                overrides = generation.get("model_parameters", {}).get(model, {})
                yield dict(base, generation_type="target", sample_index=0, parameters=generation["target"] | overrides)
                params = {k: v for k, v in generation["sampling"].items() if k not in ("count", "seeds")}
                for index, seed in enumerate(generation["sampling"]["seeds"], 1):
                    yield dict(base, generation_type="sample", sample_index=index, parameters=dict(params, seed=seed) | overrides)


def run_specs(specs, config, experiment_id, benchmark=None, retry_uncertain=False):
    validate_id(experiment_id)
    if config["groq"].get("free_plan_confirmed") is not True:
        raise RuntimeError("Free Plan confirmation is required before inference")
    store = Store(project_path(config["paths"]["ledger"]))
    client = None
    log = project_path(config["paths"]["logs"]) / f"{experiment_id}.jsonl"
    try:
        with store.writer_lock():
            client = Client(config["groq"])
            snapshot_path, value = snapshot(client, config["paths"]["snapshots"])
            requested = {spec["model_id"] for spec in specs}
            try:
                require_models(value, requested)
            except RuntimeError:
                event(log, "model_unavailable", requested=sorted(requested), snapshot=str(snapshot_path))
                raise
            splits = project_path(config["paths"]["splits"])
            meta = metadata(experiment_id, config, benchmark, splits, snapshot_path)
            # Operational ceilings may change on resume; research inputs may not.
            immutable = dict(generation=config["generation"], specs=specs,
                             benchmark_hash=file_hash(benchmark) if benchmark else None,
                             split_hash=file_hash(splits) if splits.exists() else None)
            store.register_experiment(experiment_id, immutable, meta)
            folder = project_path("experiments/pilot") / experiment_id
            folder.mkdir(parents=True, exist_ok=True)
            if not (folder / "metadata.json").exists():
                write_json(folder / "metadata.json", meta)
                write_json(folder / "config.json", config)
            if not (folder / "plan.json").exists():
                write_json(folder / "plan.json", dict(experiment_id=experiment_id, requests=specs,
                                                      expected_requests=len(specs)))
            event(log, "run_started", metadata=meta)
            new, skipped, invalid = 0, 0, 0
            try:
                for spec in specs:
                    record, created = execute(store, client, spec, config["groq"], log, retry_uncertain)
                    new += int(created)
                    skipped += int(not created)
                    invalid += int(not record["valid_response"])
                    if created:
                        write_json(folder / "progress.json", dict(new=new, skipped=skipped, invalid=invalid,
                                                                 total_planned=len(specs), last_request=record["request_id"]))
                    if not record["valid_response"]:
                        event(log, "invalid_response_retained", request_id=record["request_id"],
                              finish_reason=record["finish_reason"], complete_case_eligible=False)
                    if new and new % 50 == 0 and created:
                        store.export(project_path(config["paths"]["generations"]))
            finally:
                store.export(project_path(config["paths"]["generations"]))
                write_json(folder / "budget.json", Budget(store, config["groq"]).summary())
            result = dict(planned=len(specs), new_requests=new, skipped=skipped, invalid_responses=invalid)
            write_json(folder / "last_run.json", result)
            return result
    finally:
        if client:
            client.close()
        store.close()


def pilot(args, config):
    facts = read_benchmark(project_path(config["paths"]["benchmark"]))
    pending = [fact.fact_id for fact in facts if not fact.verified_by_human]
    if config["pilot"].get("require_human_verified") and pending and not args.dry_run:
        raise ValueError(f"Pilot awaits human verification of {len(pending)} facts; no API requests sent")
    if args.limit:
        facts = facts[:args.limit]
    models = selected_models(config, args.model)
    languages = args.language or ["en", "ru", "kk"]
    specs = list(generation_specs(facts, models, languages, config, args.experiment_id))
    if args.dry_run:
        return dict(dry_run=True, facts=len(facts), models=models, languages=languages,
                    pending_human_verification=len(pending),
                    target_requests=len(facts)*len(models)*len(languages), sample_requests=len(specs)*5//6,
                    total_requests=len(specs), judge_requests_not_included=True)
    return run_specs(specs, config, args.experiment_id, project_path(config["paths"]["benchmark"]), args.retry_uncertain)

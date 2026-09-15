from _common import main, parser
from src.generation.run import run_specs, selected_models


def run(args, config):
    models = selected_models(config, args.model)
    if len(models) != 3:
        raise ValueError("Phase 1 integration check expects three configured target models")
    specs = [dict(experiment_id=args.experiment_id, fact_id="integration_ok", language="en",
                  model_id=model, generation_type="integration", sample_index=0,
                  prompt_version="integration_v1", prompt_text="Reply with OK only.",
                  parameters=config["generation"]["target"] | config["generation"].get("model_parameters", {}).get(model, {})) for model in models]
    if args.dry_run:
        return dict(dry_run=True, requests=len(specs), models=models, research_data=False)
    result = run_specs(specs, config, args.experiment_id, retry_uncertain=args.retry_uncertain)
    if result["invalid_responses"]:
        raise RuntimeError("Integration responses include empty/truncated output; inspect saved raw responses")
    return result


if __name__ == "__main__":
    main(run, parser("Three real transport checks, excluded from research data", "integration_v1", generation=True))

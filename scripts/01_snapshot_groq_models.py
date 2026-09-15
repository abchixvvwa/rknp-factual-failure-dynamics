from _common import main, parser
from src.groq.client import Client
from src.groq.models import snapshot, require_models
from src.generation.run import selected_models


def run(args, config):
    requested = selected_models(config) + [config["models"]["semantic_judge"]["id"]]
    if args.dry_run:
        return dict(dry_run=True, requested=requested, endpoint="GET /openai/v1/models")
    client = Client(config["groq"])
    try:
        path, value = snapshot(client, config["paths"]["snapshots"])
        return dict(snapshot=str(path), configured_models_present=require_models(value, requested),
                    free_tier_access_verified=False, note="Model listing does not report the organization's billing plan")
    finally:
        client.close()


if __name__ == "__main__":
    main(run, parser("Save immutable Groq model availability snapshot"))

from _common import main, parser
from src.benchmark.validate import read_benchmark, source_checks, summary
from src.utils.io import project_path, write_json


def run(args, config):
    path = project_path(config["paths"]["benchmark"])
    facts = read_benchmark(path, main=args.main)
    result = summary(path, facts)
    if args.check_sources and not args.dry_run:
        result["sources"] = source_checks(facts[:args.limit] if args.limit else facts)
    if not args.dry_run:
        write_json(project_path("results/reports/benchmark_validation.json"), result)
    return result


if __name__ == "__main__":
    p = parser("Validate benchmark schema and provenance")
    p.add_argument("--main", action="store_true", help="Reject facts lacking human verification")
    p.add_argument("--check-sources", action="store_true", help="HEAD requests; never implies factual verification")
    main(run, p)

from _common import main, parser
from src.generation.run import pilot


if __name__ == "__main__":
    main(pilot, parser("Generate pilot targets and five samples per case", generation=True))

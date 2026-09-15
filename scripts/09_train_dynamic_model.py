from _common import main, parser
from src.modeling.train import train_family

if __name__ == "__main__":
    main(lambda args, config: train_family(args, config, "dynamic"), parser("Train three dynamic uncertainty candidates"))

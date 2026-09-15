from _common import main, parser
from src.modeling.train import select_validation

if __name__ == "__main__":
    main(select_validation, parser("Select and save the proposed model using validation AUROC"))

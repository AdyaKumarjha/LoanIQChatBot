import pandas as pd
fromconfig import DATASET_PATH


class LoanDataLoader:

    def __init__(self):
        self.df = None

    def load_data(self):
        if self.df is None:
            self.df = pd.read_excel(DATASET_PATH)

        return self.df


loan_loader = LoanDataLoader()
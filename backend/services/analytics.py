import pandas as pd
from utils.data_loader import loan_loader


class LoanAnalytics:

    def __init__(self):
        self.df = loan_loader.load_data()

    def total_cases(self):
        return int(len(self.df))

    def approved_cases(self):
        return int((self.df["Decision"] == "Approved").sum())

    def rejected_cases(self):
        return int((self.df["Decision"] == "Rejected").sum())

    def average_loan_amount(self):
        return float(self.df["Loan_Amount"].fillna(0).mean())

    def total_sanction_amount(self):
        return float(self.df["Sanction_Amount"].fillna(0).sum())

    def high_risk_cases(self):
        return int((self.df["Risk_Band"] == "High").sum())

    def priority_cases(self):
        return int((self.df["Priority_Flag"] == "High").sum())

    def branch_summary(self):
        summary = (
            self.df.groupby("Branch")
            .size()
            .sort_values(ascending=False)
        )

        return {k: int(v) for k, v in summary.items()}

    # ===============================
    # Summary for Gemini AI
    # ===============================
    def summary_for_ai(self):
        return {
            "total_cases": self.total_cases(),
            "approved_cases": self.approved_cases(),
            "rejected_cases": self.rejected_cases(),
            "high_risk_cases": self.high_risk_cases(),
            "average_loan_amount": self.average_loan_amount(),

            # Change these column names if your dataset uses different names
            "products": self.df["Product"].dropna().unique().tolist(),
            "regions": self.df["Region"].dropna().unique().tolist(),

            "branches": self.branch_summary(),
        }


analytics = LoanAnalytics()
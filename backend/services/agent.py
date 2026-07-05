from services.analytics import analytics
from services.generative_ai import ask_gemini
from models.predictive_ai import predictor


class LoanAgent:

    def execute(self, question):

        q = question.lower()

        # Sense AI
        if "branch" in q:
            return analytics.branch_summary()

        if "risk" in q:
            return analytics.high_risk_cases()

        # Predictive AI
        if "predict loan" in q:
            sample = {
                "Loan_Amount": 500000,
                "Property_Value": 800000,
                "Bureau_Score": 760,
                "FOIR_%": 35,
                "Region": "North",
                "Product": "Home Loan",
                "Customer_Type": "Salaried",
                "Risk_Band": "Low"
            }

            result = predictor.predict(sample)
            return f"Predicted Loan Decision: {result}"

        # Generative AI
        return ask_gemini(question)


agent = LoanAgent()
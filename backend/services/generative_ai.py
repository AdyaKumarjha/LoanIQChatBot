import google.generativeai as genai

from config import GEMINI_API_KEY
from services.analytics import analytics

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(question: str):

    summary = analytics.summary_for_ai()

    # print("Products:", summary["products"])
    # print("Product types:", [type(x) for x in summary["products"]])

    # print("Regions:", summary["regions"])
    # print("Region types:", [type(x) for x in summary["regions"]])

    prompt = f"""
You are an AI Loan Business Analyst.

You analyze loan portfolios and provide:
- Business insights
- Risk analysis
- Recommendations
- Approval trends
- Branch performance
- Executive summaries

Answer professionally using the provided data.
If the user asks for recommendations, explain the reasoning.

You have the following loan portfolio summary.

Total Loan Cases: {summary['total_cases']}
Approved Cases: {summary['approved_cases']}
Rejected Cases: {summary['rejected_cases']}
High Risk Cases: {summary['high_risk_cases']}
Average Loan Amount: ₹{summary['average_loan_amount']:,.2f}

Products:
{', '.join(map(str, summary['products']))}

Regions:
{', '.join(map(str, summary['regions']))}

Total Branches:
{summary['branches']}

User Question:
{question}

Give a professional business answer.
"""

    response = model.generate_content(prompt)

    return response.text
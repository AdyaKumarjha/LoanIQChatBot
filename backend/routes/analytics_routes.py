from fastapi import APIRouter
from services.analytics import analytics

router = APIRouter(prefix="/analytics", tags=["Sense AI"])


@router.get("/summary")
def summary():

    return {
        "TotalCases": int(analytics.total_cases()),
        "ApprovedCases": int(analytics.approved_cases()),
        "RejectedCases": int(analytics.rejected_cases()),
        "AverageLoanAmount": float(analytics.average_loan_amount()),
        "TotalSanctionAmount": float(analytics.total_sanction_amount()),
        "HighRiskCases": int(analytics.high_risk_cases()),
        "HighPriorityCases": int(analytics.priority_cases())
    }


@router.get("/branches")
def branches():
    return analytics.branch_summary()
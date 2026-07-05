from fastapi import APIRouter
from pydantic import BaseModel, Field

frommodels.predictive_ai import predictor

router = APIRouter(tags=["Prediction"])


class PredictionRequest(BaseModel):
    Region: str
    Product: str
    Customer_Type: str
    Loan_Amount: float
    Property_Value: float
    Bureau_Score: int
    FOIR_: float = Field(alias="FOIR_%")

    model_config = {
        "populate_by_name": True
    }


@router.post("/predict")
def predict_loan(request: PredictionRequest):

    prediction = predictor.predict(request.model_dump())

    return {
        "prediction": prediction
    }
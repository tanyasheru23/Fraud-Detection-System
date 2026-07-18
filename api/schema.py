from pydantic import BaseModel

class Transaction(BaseModel):
    step: int
    type: str
    amount: float
    nameOrig: str
    oldbalanceOrg: float
    newbalanceOrig: float
    nameDest: str
    oldbalanceDest: float
    newbalanceDest: float


class FraudPrediction(BaseModel):
    is_fraud: bool
    fraud_percentage: float
    prediction: str
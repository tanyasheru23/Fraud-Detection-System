"""
FastAPI application for the Online Payment Fraud Detection project.

This module exposes REST API endpoints for predicting fraudulent
transactions using the trained Random Forest model.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .schema import Transaction, FraudPrediction
from src.inference import predict


app = FastAPI(
    title="Online Payment Fraud Detection API",
    description="REST API for predicting fraudulent online payment transactions.",
    version="1.0.0"
)

templates = Jinja2Templates(directory="api/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)

@app.post(
    "/predict",
    response_model=FraudPrediction
)
def prediction_result(transaction: Transaction):
    """
    Predict whether a transaction is fraudulent.
    """

    try:

        prediction, probability = predict(
            transaction.model_dump()
        )

        result = (
            "Fraud Transaction"
            if prediction == 1
            else "Legitimate Transaction"
        )

        return FraudPrediction(
            is_fraud=bool(prediction),
            fraud_percentage=round(probability * 100, 2),
            prediction=result
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
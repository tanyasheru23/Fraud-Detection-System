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
from fastapi.staticfiles import StaticFiles
from src.utils import load_model

model, feature_columns, explainer = load_model()

app = FastAPI(
    title="Online Payment Fraud Detection API",
    description="REST API for predicting fraudulent online payment transactions.",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="api/static"),
    name="static"
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

        prediction, probability, top_features = predict(
            transaction.model_dump(),
            model,
            feature_columns,
            explainer
        )

        result = (
            "Fraud Transaction"
            if prediction == 1
            else "Legitimate Transaction"
        )

        return FraudPrediction(
            is_fraud=bool(prediction),
            fraud_percentage=round(probability * 100, 2),
            prediction=result,
            top_features=top_features
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
"""
Inference pipeline for the Online Payment Fraud Detection project.

This module loads the trained model, performs feature engineering and
preprocessing on new transaction data, and predicts whether the
transaction is fraudulent.
"""

import pandas as pd

from .feature_engineering import feature_engineer
from .pre_processing import process
from .utils import load_model


def predict(data: dict):
    """
    Predict whether a transaction is fraudulent.

    Args:
        data (dict):
            Transaction details.

    Returns:
        tuple:
            prediction (int)
            probability (float)
    """

    # Convert input dictionary to DataFrame
    data_df = pd.DataFrame([data])

    # Feature Engineering
    data_df = feature_engineer(data_df)

    # Preprocessing
    data_df = process(data_df)

    # Load trained model and feature columns
    model, feature_columns = load_model()

    # Match training feature order
    data_df = data_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(data_df)[0]
    probability = model.predict_proba(data_df)[0][1]

    return prediction, probability


def main():
    """
    Example inference using a sample transaction.
    """

    non_fraud_sample = {
        "step": 1,
        "type": "PAYMENT",
        "amount": 11668.14,
        "nameOrig": "C2048537720",
        "oldbalanceOrg": 41554.0,
        "newbalanceOrig": 29885.86,
        "nameDest": "M1230701703",
        "oldbalanceDest": 0.0,
        "newbalanceDest": 0.0
    }

    fraud_sample = {
        "step": 44,
        "type": "TRANSFER",
        "amount": 534255.94,
        "nameOrig": "C967325382",
        "oldbalanceOrg": 534255.94,
        "newbalanceOrig": 0.0,
        "nameDest": "C1259079602",
        "oldbalanceDest": 0.0,
        "newbalanceDest": 0.0
    }

    prediction, probability = predict(fraud_sample)

    print("=" * 40)
    print("Fraud Detection Result")
    print("=" * 40)

    print(f"Fraud Probability : {probability:.2%}")

    if prediction == 1:
        print("Prediction : Fraud Transaction")
    else:
        print("Prediction : Legitimate Transaction")


if __name__ == "__main__":
    main()
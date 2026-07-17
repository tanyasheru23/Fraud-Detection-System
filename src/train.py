"""
Model training pipeline for the Online Payment Fraud Detection project.

This module loads the dataset, performs feature engineering and preprocessing,
trains the optimized Random Forest model, evaluates its performance,
and computes feature importance.
"""

import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)
from sklearn.model_selection import train_test_split

from .feature_engineering import feature_engineer
from .pre_processing import process
from .utils import save_model, save_results
from .config import RF_PARAMS


def load_data(filepath):
    """
    Load the dataset from disk.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    return pd.read_csv(filepath)


def train_model(X_train, y_train):
    """
    Train the optimized Random Forest model.

    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training labels.

    Returns:
        RandomForestClassifier: Trained model.
    """
    model = RandomForestClassifier(**RF_PARAMS)
    model.fit(X_train, y_train)

    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model.

    Args:
        model: Trained model.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): Test labels.

    Returns:
        dict: Evaluation metrics.
    """

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1": f1_score(y_test, y_pred),
        "ROC_AUC": roc_auc_score(y_test, y_prob)
    }

    return metrics, y_pred


def get_feature_importance(model, feature_names):
    """
    Compute feature importance scores.

    Args:
        model: Trained Random Forest model.
        feature_names (list): Feature column names.

    Returns:
        pd.Series: Sorted feature importance scores.
    """

    return (
        pd.Series(
            model.feature_importances_,
            index=feature_names
        )
        .sort_values(ascending=False)
    )


def train():
    """
    Execute the complete training pipeline.

    Returns:
        tuple:
            model (RandomForestClassifier)
            results (dict)
            feature_importance (pd.Series)
            X_train (pd.DataFrame)
    """

    print("Loading Dataset...")
    df = load_data(
        "data/raw/onlinefraud/onlinefraud.csv"
    )

    print("Performing Feature Engineering...")
    df = feature_engineer(df)

    print("Preprocessing Data...")
    df = process(df)

    # Features and Target
    X = df.drop(columns=["isFraud"])
    y = df["isFraud"]

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )

    print("Training Random Forest...")
    model = train_model(X_train, y_train)

    print("\nTraining Performance")
    print("=" * 50)

    train_metrics, _ = evaluate_model(
        model,
        X_train,
        y_train
    )

    for metric, value in train_metrics.items():
        print(f"{metric:<12}: {value:.6f}")

    
    # Evaluation
    print("\nTest Performance")
    print("=" * 50)

    test_metrics, y_pred = evaluate_model(
        model,
        X_test,
        y_test
    )

    for metric, value in test_metrics.items():
        print(f"{metric:<12}: {value:.6f}")

    print("\nClassification Report")
    print("=" * 50)

    
    report = classification_report(
        y_test,
        y_pred,
        digits=4
    )
    print(report)

    print("\nConfusion Matrix")
    print("=" * 50)

    
    confusionMatrix = confusion_matrix(
        y_test,
        y_pred
    )
    print(confusionMatrix)

    feature_importance = get_feature_importance(
        model,
        X_train.columns
    )

    save_results(
        train_metrics,
        test_metrics,
        report,
        confusionMatrix,
        feature_importance
    )

    print("\nTop 15 Important Features")
    print("=" * 50)

    print(feature_importance.head(15))

    return (
        model,
        feature_importance,
        list(X_train.columns)
    )


def main():
    """
    Train the model and display evaluation results.
    """

    model, feature_importance, feature_columns = train()

    save_model(model, feature_columns)

    print("\nTraining Pipeline Completed Successfully.")

if __name__ == "__main__":
    main()
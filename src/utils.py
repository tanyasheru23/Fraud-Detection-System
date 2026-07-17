import joblib
import json
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def save_model(model, feature_columns):
    print("Saving Model...")
    joblib.dump(model, "models/fraud_detector_rf.pkl")
    joblib.dump(list(feature_columns), "models/feature_columns.pkl")


def save_results(
    train_metrics,
    test_metrics,
    report,
    confusion,
    feature_importance
):
    """
    Save evaluation artifacts generated during model training.

    Args:
        train_metrics (dict)
        test_metrics (dict)
        report (str)
        confusion (np.ndarray)
        feature_importance (pd.Series)
    """

    print("Saving results...")
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    # Metrics
    with open(results_dir / "metrics.json", "w") as f:
        json.dump(
            {
                "train": train_metrics,
                "test": test_metrics
            },
            f,
            indent=4
        )

    # Classification Report
    with open(results_dir / "classification_report.txt", "w") as f:
        f.write(report)

    # Confusion Matrix
    pd.DataFrame(confusion).to_csv(
        results_dir / "confusion_matrix.csv",
        index=False
    )

    # Feature Importance CSV
    feature_importance.to_csv(
        results_dir / "feature_importance.csv",
        header=["importance"]
    )

    # Feature Importance Plot
    plt.figure(figsize=(8,6))

    feature_importance.head(15)\
        .sort_values()\
        .plot(kind="barh")

    plt.title("Top 15 Important Features")
    plt.xlabel("Importance")

    plt.tight_layout()

    plt.savefig(
        results_dir / "feature_importance.png",
        dpi=300
    )

    plt.close()

def load_model():
    """
    Load the trained model and feature column names.

    Returns:
        tuple:
            model
            feature_columns
    """

    model = joblib.load("models/fraud_detector_rf.pkl")
    feature_columns = joblib.load("models/feature_columns.pkl")

    return model, feature_columns
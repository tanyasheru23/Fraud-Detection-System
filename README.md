# Online Payment Fraud Detection

A production-style Machine Learning project for detecting fraudulent online payment transactions using feature engineering, ensemble learning, and a modular FastAPI inference pipeline.

> **Project Status**
>
> - Exploratory Data Analysis (EDA) ✅
> - Feature Engineering ✅
> - Model Training & Evaluation ✅
> - Modular Python Package ✅
> - Model Serialization & Inference Pipeline ✅
> - FastAPI Backend ✅
> - Frontend 🚧
> - Docker Deployment 🚧

---

# Project Overview

Online payment fraud poses a significant challenge due to its highly imbalanced nature and the financial losses associated with fraudulent transactions.

This project implements an end-to-end fraud detection pipeline, covering the complete machine learning workflow:

- Exploratory Data Analysis
- Feature Engineering
- Data Preprocessing
- Model Training
- Hyperparameter Optimization
- Model Evaluation
- Feature Importance Analysis
- Model Serialization
- Reusable Inference Pipeline
- REST API using FastAPI

The notebook implementation has been refactored into a modular Python package, making it suitable for deployment and real-world inference.

---

# Dataset

- **Source:** Kaggle – PaySim Mobile Money Simulation Dataset
- **Transactions:** ~6.3 Million
- **Fraud Rate:** ~0.12%
- **Task:** Binary Classification

---

# Project Structure

```text
Fraud-Detection-System/
│
├── api/
│   ├── main.py
│   ├── schema.py
│   └── templates/
│       └── index.html
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── results/
│
├── src/
│   ├── config.py
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── inference.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── Dockerfile
```

---

# Machine Learning Pipeline

- Exploratory Data Analysis
- Feature Engineering
- Data Preprocessing
- Baseline Model Training
- Hyperparameter Optimization
- Model Evaluation
- Feature Importance Analysis
- Model Serialization
- FastAPI Inference Pipeline

---

# Models Evaluated

- Logistic Regression
- Random Forest
- XGBoost

After experimentation and hyperparameter optimization, the optimized Random Forest model was selected as the final production model.

---

# Feature Engineering

Several domain-inspired features were engineered, including:

- Balance Difference
- Balance Error
- Transaction Fraction
- Fraction Used
- Remaining Fraction
- Full Balance Transfer
- Zero Balance Indicators
- Balance Change Indicators
- Cash Transfer Indicator

These engineered features significantly improved fraud detection performance compared to using the raw dataset alone.

---

# Model Performance

| Metric | Score |
|---------|-------:|
| Accuracy | **99.9997%** |
| Precision | **100.00%** |
| Recall | **99.76%** |
| F1 Score | **99.88%** |
| ROC-AUC | **99.92%** |

The optimized Random Forest generalized well on unseen data while missing only four fraudulent transactions in the held-out test set.

---

# Installation

Clone the repository

```bash
git clone https://github.com/tanyasheru23/Fraud-Detection-System.git

cd Fraud-Detection-System
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the dependencies

```bash
pip install -r requirements.txt
```

---

# Training

Place the PaySim dataset inside:

```text
data/raw/
```

Run the training pipeline

```bash
python -m src.train
```

Training automatically:

- Performs feature engineering
- Preprocesses the dataset
- Trains the optimized Random Forest model
- Evaluates model performance
- Saves the trained model
- Saves feature columns
- Stores evaluation artifacts inside the `results/` directory

---

# Running the API

Start the FastAPI server

```bash
uvicorn api.main:app --reload
```

Once the server starts:

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

Home Page

```
http://127.0.0.1:8000/
```

---

# Example Prediction Request

```json
{
    "step": 1,
    "type": "TRANSFER",
    "amount": 181.00,
    "nameOrig": "C123456789",
    "oldbalanceOrg": 181.00,
    "newbalanceOrig": 0.00,
    "nameDest": "C987654321",
    "oldbalanceDest": 0.00,
    "newbalanceDest": 181.00
}
```

---

# Example API Response

```json
{
    "is_fraud": true,
    "fraud_percentage": 99.87,
    "prediction": "Fraud Transaction"
}
```

---

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- FastAPI
- Pydantic
- Joblib

---

# Current Progress

## Completed

- End-to-End Exploratory Data Analysis
- Feature Engineering
- Data Preprocessing Pipeline
- Model Training & Evaluation
- Hyperparameter Optimization
- Feature Importance Analysis
- Model Serialization
- Reusable Inference Pipeline
- FastAPI Backend

## Upcoming

- Interactive Frontend
- Docker Containerization
- Cloud Deployment
- SHAP Explainability
- Real-time Prediction Dashboard

---

# Future Improvements

- SHAP-based Explainability
- Drift Detection
- Model Monitoring
- Sequence-aware Fraud Detection
- Real-time Streaming Inference
- CI/CD Pipeline
- Cloud Deployment

# Online Payment Fraud Detection

A production-style Machine Learning project for detecting fraudulent online payment transactions using feature engineering, ensemble learning, FastAPI, and an interactive web interface.

> **Project Status**
>
> - Exploratory Data Analysis (EDA) ✅
> - Feature Engineering ✅
> - Model Training & Evaluation ✅
> - Modular Python Package ✅
> - Model Serialization & Inference Pipeline ✅
> - FastAPI Backend ✅
> - Interactive Frontend ✅

---

# Project Overview

Online payment fraud is a highly imbalanced binary classification problem with significant financial implications.

This project implements an end-to-end machine learning pipeline that transforms a research notebook into a production-style application. It includes data preprocessing, feature engineering, model optimization, a reusable inference pipeline, a REST API using FastAPI, and an interactive frontend for real-time fraud prediction.

---

# Features

- Exploratory Data Analysis (EDA)
- Domain-inspired Feature Engineering
- Data Preprocessing Pipeline
- Random Forest Hyperparameter Optimization
- Model Evaluation
- Feature Importance Analysis
- Model Serialization using Joblib
- Modular Python Package
- REST API using FastAPI
- Interactive HTML/CSS/JavaScript Frontend
- Real-time Fraud Prediction

---

# Dataset

- **Source:** Kaggle – PaySim Mobile Money Simulation Dataset
- **Transactions:** ~6.3 Million
- **Fraud Rate:** ~0.12%
- **Problem Type:** Binary Classification

---

# Project Structure

```text
Fraud-Detection-System/
│
├── api/
│   ├── main.py
│   ├── schema.py
│   ├── templates/
│   │     └── index.html
│   └── static/
│         ├── style.css
│         └── script.js
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

```
Raw Dataset
      │
      ▼
Feature Engineering
      │
      ▼
Preprocessing
      │
      ▼
Random Forest
      │
      ▼
Model Serialization
      │
      ▼
SHAP Explainability
      │
      ▼
FastAPI Backend
      │
      ▼
Interactive Frontend
```

---

# Models Evaluated

- Logistic Regression
- Random Forest
- XGBoost

Following experimentation and hyperparameter optimization, the **Random Forest** model was selected as the final production model.

---

# Engineered Features

- Balance Difference
- Balance Error
- Fraction Used
- Remaining Fraction
- Transaction Fraction
- Cash Transfer Indicator
- Full Balance Transfer
- Zero Balance Indicators
- Balance Change Indicators

These engineered features significantly improved fraud detection performance over the original feature set.

---

# Model Performance

| Metric | Score |
|---------|-------:|
| Accuracy | **99.9997%** |
| Precision | **100.00%** |
| Recall | **99.76%** |
| F1 Score | **99.88%** |
| ROC-AUC | **99.92%** |

The optimized Random Forest generalized well on unseen data while missing only four fraudulent transactions in the held-out test dataset.

---

## Model Explainability

To improve prediction transparency, the project integrates **SHAP (SHapley Additive Explanations)** for local model interpretability.

For every prediction, the API identifies the three most influential engineered features contributing to the model's decision. These explanations are returned alongside the fraud probability and displayed in the frontend, allowing users to understand *why* a transaction was classified as fraudulent or legitimate.

Example explanation:

- Entire Balance Transferred (75.6%)
- Origin Balance Error (15.9%)
- Fraction of Balance Used (8.5%)

This makes the model more interpretable and suitable for real-world financial applications where prediction transparency is important.

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

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Training

Place the PaySim dataset inside

```
data/raw/
```

Run

```bash
python -m src.train
```

The training pipeline automatically

- Performs feature engineering
- Applies preprocessing
- Trains the optimized Random Forest model
- Evaluates model performance
- Saves the trained model
- Saves feature columns
- Stores evaluation artifacts

---

# Running the Application

Start the FastAPI server

```bash
uvicorn api.main:app --reload
```

Application

```
http://127.0.0.1:8000/
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
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
# Web Page - Example Fraud Predictions

### Legitimate Transaction
<img width="1918" height="857" alt="Screenshot 2026-07-19 203408" src="https://github.com/user-attachments/assets/3eaba7fb-e441-459d-88e3-1d67186826de" />

### Fraud Transaction
<img width="1918" height="862" alt="Screenshot 2026-07-19 203245" src="https://github.com/user-attachments/assets/019436f4-28d8-4e30-b7bc-7486e4ac80de" />


---

# Tech Stack

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- SHAP

### Backend

- FastAPI
- Pydantic

### Frontend

- HTML5
- CSS3
- JavaScript

### Visualization

- Matplotlib
- Seaborn

---

# Current Progress

## Completed

- End-to-End Exploratory Data Analysis
- Feature Engineering
- Data Preprocessing
- Model Training
- Hyperparameter Optimization
- Feature Importance Analysis
- Model Serialization
- Reusable Inference Pipeline
- SHAP Explainability
- FastAPI Backend
- Interactive Frontend

---

# Future Improvements

- Model Monitoring
- Drift Detection
- Streaming Fraud Detection
- Sequence-aware Fraud Detection
- Explainability Dashboard
- CI/CD Pipeline

---

## License

This project is intended for educational and portfolio purposes.

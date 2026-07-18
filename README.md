# Online Payment Fraud Detection

A production-style Machine Learning project for detecting fraudulent online payment transactions using feature engineering, ensemble learning, and a modular inference pipeline.

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
- Model Serialization
- Reusable Inference Pipeline

The project has been refactored from a notebook into a modular Python package, making it suitable for deployment through a REST API.

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
├── api/                 # FastAPI backend (WIP)
│   ├── main.py
│   ├── schema.py
│   ├── templates/
│   │   ├── index.html
├── data/
├── models/
├── notebooks/
├── results/
├── src/
│   ├── config.py
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── inference.py
│   └── utils.py
│
├── README.md
├── requirements.txt
└── Dockerfile
```

---

# Machine Learning Pipeline

- Exploratory Data Analysis
- Feature Engineering
- Data Preprocessing
- Random Forest Training
- Hyperparameter Optimization
- Model Evaluation
- Feature Importance Analysis
- Model Serialization
- Inference Pipeline

---

# Models Evaluated

- Logistic Regression
- Random Forest
- XGBoost

After experimentation and hyperparameter tuning, the optimized Random Forest model was selected as the final production model.

---

# Feature Engineering

Domain-inspired features include:

- Balance Difference
- Balance Error
- Transaction Fraction
- Fraction Used
- Remaining Fraction
- Full Balance Transfer
- Zero Balance Indicators
- Balance Change Indicators
- Cash Transfer Indicator

---

# Model Performance

| Metric | Score |
|---------|-------:|
| Accuracy | **99.9997%** |
| Precision | **100.00%** |
| Recall | **99.76%** |
| F1 Score | **99.88%** |
| ROC-AUC | **99.92%** |

The optimized Random Forest generalized well on unseen data with nearly identical training and testing performance while missing only four fraudulent transactions in the held-out test set.

---

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Joblib
- FastAPI 

---

# Current Progress

Completed

- End-to-End EDA
- Feature Engineering
- Data Preprocessing
- Model Training
- Hyperparameter Optimization
- Model Evaluation
- Feature Importance Analysis
- Model Serialization
- Reusable Inference Pipeline
- FastAPI Backend

Upcoming

- Interactive Frontend
- Docker Containerization
- Cloud Deployment
- SHAP Explainability
- Real-time Prediction API

---

# Future Improvements

- SHAP-based Explainability
- Drift Detection
- Model Monitoring
- Sequence-aware Fraud Detection
- Real-time Streaming Inference
- CI/CD Pipeline

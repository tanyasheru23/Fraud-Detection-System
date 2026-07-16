# Online Payment Fraud Detection

A machine learning project for detecting fraudulent online payment transactions using exploratory data analysis, feature engineering, and ensemble learning methods.

> **Status:** Notebook Version Completed ✅  
> Repository structure, API, deployment, and frontend will be added in the next phase.

---

## Project Overview

Online payment fraud causes significant financial losses and presents a highly imbalanced classification problem. This project explores the complete machine learning workflow, from understanding the data through Exploratory Data Analysis (EDA) to feature engineering, model training, hyperparameter optimization, and model interpretation.

The primary objective is not only to build an accurate fraud detection model but also to understand the characteristics of fraudulent transactions and engineer meaningful features from domain knowledge.

---

## Dataset

- **Source:** Kaggle - PaySim Mobile Money Simulation Dataset
- **Transactions:** ~6.3 Million
- **Fraud Rate:** ~0.12%
- **Problem Type:** Binary Classification (Fraud / Non-Fraud)

---

## Workflow

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Baseline Model Training
- Hyperparameter Optimization
- Model Evaluation
- Feature Importance Analysis

---

## Models Evaluated

- Logistic Regression
- Random Forest
- XGBoost

Random Forest was selected as the final model after hyperparameter optimization.

---

## Feature Engineering

Several domain-inspired features were engineered, including:

- Balance Difference
- Balance Error
- Full Balance Transfer
- Transaction Fraction
- Fraction Used
- Remaining Fraction
- Cash Transfer Indicator

Feature importance analysis showed that these engineered features contributed significantly to model performance.

---

## Results

The optimized Random Forest achieved excellent performance on the test dataset:

| Metric | Score |
|--------|------:|
| Accuracy | 99.9997% |
| Precision | 100.00% |
| Recall | 99.76% |
| F1 Score | 99.88% |
| ROC-AUC | 99.94% |

---

## Repository (Work in Progress)

The notebook is currently available in this repository.

The next phase of the project will include:

- Model serialization
- Modular Python package
- FastAPI backend
- Interactive frontend
- Docker support
- Cloud deployment

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook

---

## Future Improvements

- SHAP Explainability
- Real-time Fraud Detection API
- Docker Deployment
- Interactive Dashboard
- Drift Monitoring
- Sequence-based Fraud Detection

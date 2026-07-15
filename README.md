# 💳 Credit Card Fraud Detection using Machine Learning

An end-to-end Machine Learning web application for detecting fraudulent credit card transactions using multiple classification models. The application compares the performance of several Machine Learning and Deep Learning models and deploys the best-performing Random Forest model through an interactive Streamlit dashboard.

---

## Features

- Real-time credit card fraud prediction
- Interactive Streamlit web interface
- Comparison of multiple ML/DL models
- Dataset analysis dashboard
- Feature importance visualization
- ROC Curve & Precision-Recall Curve
- Confidence score and fraud probability prediction

---

## Machine Learning Workflow

1. Data Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Scaling
4. Handling Class Imbalance using SMOTE
5. Model Training
6. Model Evaluation
7. Model Comparison
8. Random Forest Deployment

---

## Models Evaluated

- Logistic Regression
- Decision Tree
- Naive Bayes
- Random Forest
- XGBoost
- Artificial Neural Network (ANN)
- Autoencoder

---

## Performance Summary

| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|-------|---------:|----------:|-------:|---------:|--------:|
| Logistic Regression | 0.9741 | 0.0578 | 0.9184 | 0.1088 | 0.9463 |
| Decision Tree | 0.9973 | 0.3737 | 0.7551 | 0.5000 | 0.8765 |
| Naive Bayes | 0.9744 | 0.0561 | 0.8776 | 0.1055 | 0.9261 |
| Random Forest | **0.9995** | **0.8710** | 0.8265 | **0.8482** | 0.9132 |
| XGBoost | 0.9973 | 0.3744 | 0.8673 | 0.5231 | 0.9324 |
| ANN | 0.9988 | 0.6058 | 0.8469 | 0.7064 | 0.9230 |

---

## Technology Stack

### Machine Learning
- Scikit-learn
- TensorFlow / Keras
- XGBoost
- SMOTE

### Data Processing
- Pandas
- NumPy

### Visualization
- Matplotlib

### Web Application
- Streamlit

---

## Project Structure

```text
Credit_Card_Fraud_Detection_Web/
│
├── app.py
├── predict.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── random_forest_model.pkl
│   └── scaler.pkl
│
├── assets/
│
└── pages/
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate into the project

```bash
cd Credit_Card_Fraud_Detection_Web
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Dataset

The application uses the **Credit Card Fraud Detection Dataset**, containing anonymized European credit card transactions with highly imbalanced classes.

---

## Author

**Raghav Nimgaonkar**

Computer Science & Engineering  
VNIT Nagpur
# 💳 Credit Card Fraud Detection using Machine Learning

An end-to-end Machine Learning web application that detects fraudulent credit card transactions using multiple classification models. The application evaluates several Machine Learning and Deep Learning models and deploys the best-performing **Random Forest** classifier through an interactive Streamlit dashboard.

---

## 🚀 Live Demo

**Web Application:**  
https://creditcardfrauddetectionweb-zcowudkvjea6265fkbssqu.streamlit.app/

**GitHub Repository:**  
https://github.com/<your-username>/Credit_Card_Fraud_Detection_Web

---

## ✨ Features

- Real-time credit card fraud prediction
- Interactive Streamlit dashboard
- Comparison of multiple Machine Learning and Deep Learning models
- Dataset analysis and visualization
- Feature importance analysis
- ROC Curve and Precision-Recall Curve visualization
- Fraud probability and prediction confidence
- Multi-page analytics dashboard

---

## 🤖 Machine Learning Workflow

1. Data Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Scaling
4. Class Imbalance Handling using SMOTE
5. Model Training
6. Model Evaluation
7. Performance Comparison
8. Random Forest Deployment

---

## 📊 Models Evaluated

- Logistic Regression
- Decision Tree
- Naive Bayes
- Random Forest
- XGBoost
- Artificial Neural Network (ANN)
- Autoencoder

---

## 📈 Performance Summary

| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|-------|---------:|----------:|-------:|---------:|--------:|
| Logistic Regression | 0.9741 | 0.0578 | 0.9184 | 0.1088 | 0.9463 |
| Decision Tree | 0.9973 | 0.3737 | 0.7551 | 0.5000 | 0.8765 |
| Naive Bayes | 0.9744 | 0.0561 | 0.8776 | 0.1055 | 0.9261 |
| **Random Forest** | **0.9995** | **0.8710** | **0.8265** | **0.8482** | **0.9132** |
| XGBoost | 0.9973 | 0.3744 | 0.8673 | 0.5231 | 0.9324 |
| ANN | 0.9988 | 0.6058 | 0.8469 | 0.7064 | 0.9230 |

---

## 🛠️ Technology Stack

### Programming Language
- Python

### Machine Learning & Deep Learning
- Scikit-learn
- TensorFlow / Keras
- XGBoost
- Random Forest
- SMOTE

### Data Processing
- Pandas
- NumPy

### Data Visualization
- Matplotlib

### Web Framework
- Streamlit

---

## 📂 Project Structure

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
│   ├── model_metrics.csv
│   ├── dataset_info.csv
│   ├── feature_importance.csv
│   ├── roc_curve.png
│   ├── pr_curve.png
│   ├── feature_importance.png
│   └── class_distribution.png
│
└── pages/
    ├── About.py
    ├── Dataset_Analysis.py
    ├── Developer.py
    ├── Feature_Importance.py
    └── Model_Comparison.py
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/Credit_Card_Fraud_Detection_Web.git
```

Navigate to the project directory

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

## 📌 Dataset

This application uses the **Credit Card Fraud Detection Dataset**, which contains anonymized European credit card transactions. The dataset is highly imbalanced, making fraud detection a challenging binary classification problem.

---

## 🌐 Application Modules

- **Prediction** – Real-time fraud detection using the deployed Random Forest model.
- **Model Comparison** – Performance comparison of all trained ML/DL models.
- **Dataset Analysis** – Dataset overview, statistics, and class distribution.
- **Feature Importance** – Visualization of the most influential features in the Random Forest model.
- **About** – Overview of the workflow and technology stack.
- **Developer** – Developer profile and technical expertise.

---

## 👨‍💻 Author

**Raghav Nimgaonkar**

Computer Science & Engineering  
Visvesvaraya National Institute of Technology (VNIT), Nagpur


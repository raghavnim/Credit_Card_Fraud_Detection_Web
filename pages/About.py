import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About Credit Card Fraud Detection")

st.write("""
An intelligent fraud detection platform that leverages Machine Learning to identify
suspicious credit card transactions in real time. The application combines predictive
analytics, model evaluation, and interactive visualizations to support accurate and
interpretable fraud detection.
""")

st.markdown("---")

# ===========================
# Platform Overview
# ===========================

st.header("Platform Overview")

st.write("""
The platform analyzes transaction data and predicts whether a transaction is
fraudulent or legitimate using a trained Random Forest classifier.

In addition to real-time prediction, the application provides detailed insights
into dataset characteristics, model performance, feature importance, and
evaluation metrics, allowing users to understand both the prediction process
and the effectiveness of the underlying machine learning models.
""")

st.markdown("---")

# ===========================
# Core Capabilities
# ===========================

st.header("Core Capabilities")

col1, col2 = st.columns(2)

with col1:
    st.success("""
✔ Real-Time Fraud Prediction

✔ Confidence Score

✔ Fraud Probability Estimation

✔ Interactive Prediction Interface
""")

with col2:
    st.success("""
✔ Model Performance Comparison

✔ ROC Curve Analysis

✔ Precision-Recall Analysis

✔ Feature Importance Visualization
""")

st.markdown("---")

# ===========================
# Machine Learning Pipeline
# ===========================

st.header("Machine Learning Pipeline")

st.markdown("""
1. Data Collection

2. Data Preprocessing

3. Exploratory Data Analysis

4. Feature Scaling

5. Class Balancing using SMOTE

6. Model Training

7. Model Evaluation

8. Real-Time Fraud Prediction
""")

st.markdown("---")

# ===========================
# Models Evaluated
# ===========================

st.header("Models Evaluated")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- Logistic Regression

- Decision Tree

- Naive Bayes

- Random Forest
""")

with col2:
    st.markdown("""
- XGBoost

- Artificial Neural Network (ANN)

- Autoencoder
""")

st.markdown("---")

# ===========================
# Technology Stack
# ===========================

st.header("Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.info("""
Python

Pandas

NumPy

Scikit-learn
""")

with tech2:
    st.info("""
TensorFlow

XGBoost

SMOTE

Joblib
""")

with tech3:
    st.info("""
Streamlit

Matplotlib

Machine Learning

Data Visualization
""")

st.markdown("---")

# ===========================
# Performance Summary
# ===========================

st.header("Deployment Model")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Deployed Model", "Random Forest")

with col2:
    st.metric("Accuracy", "99.95%")

with col3:
    st.metric("ROC AUC", "0.9132")

st.markdown("---")

st.caption(
    "Designed for interactive fraud detection, model evaluation, and machine learning interpretability."
)
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Dataset Analysis")

st.write(
    "Explore the characteristics of the credit card transaction dataset used for fraud detection."
)

st.markdown("---")

# =========================
# Dataset Overview
# =========================

st.subheader("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Transactions", "284,807")

with col2:
    st.metric("Fraud Cases", "492")

with col3:
    st.metric("Legitimate", "284,315")

with col4:
    st.metric("Fraud Rate", "0.172%")

st.markdown("---")

# =========================
# Dataset Information
# =========================

st.subheader("Dataset Statistics")

info = pd.read_csv("assets/dataset_info.csv")

st.dataframe(info, use_container_width=True)

st.markdown("---")

# =========================
# Class Distribution
# =========================

st.subheader("Class Distribution")

st.image(
    "assets/class_distribution.png",
    use_container_width=True
)

st.info(
    """
The dataset is highly imbalanced.

• Legitimate Transactions: 284,315

• Fraudulent Transactions: 492

SMOTE (Synthetic Minority Oversampling Technique) was applied during
training to improve model learning.
"""
)

st.markdown("---")

# =========================
# Key Observations
# =========================

st.subheader("Key Observations")

st.success("""
✔ Highly imbalanced dataset

✔ PCA-transformed features (V1–V28)

✔ Time and Amount retained in original form

✔ Missing Values: 0

✔ Duplicate Records: Removed during preprocessing

✔ Dataset suitable for binary classification
""")
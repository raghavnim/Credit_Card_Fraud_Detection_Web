import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Model Comparison",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Model Performance Comparison")

st.write("""
Performance comparison of all machine learning and deep learning models
trained on the Credit Card Fraud Detection dataset.
""")

# -----------------------------
# Load Model Metrics
# -----------------------------
comparison = pd.read_csv("assets/model_metrics.csv")

st.subheader("Performance Metrics")

st.dataframe(
    comparison,
    use_container_width=True
)

# -----------------------------
# Accuracy Comparison
# -----------------------------
st.subheader("Accuracy Comparison")

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(comparison["ModelName"], comparison["Accuracy"])
ax.set_ylabel("Accuracy")
ax.set_ylim(0.9,1.0)
plt.xticks(rotation=25)

st.pyplot(fig)

# -----------------------------
# Precision Comparison
# -----------------------------
st.subheader("Precision Comparison")

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(comparison["ModelName"], comparison["Precision"])
ax.set_ylabel("Precision")
plt.xticks(rotation=25)

st.pyplot(fig)

# -----------------------------
# Recall Comparison
# -----------------------------
st.subheader("Recall Comparison")

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(comparison["ModelName"], comparison["Recall"])
ax.set_ylabel("Recall")
plt.xticks(rotation=25)

st.pyplot(fig)

# -----------------------------
# F1 Score Comparison
# -----------------------------
st.subheader("F1 Score Comparison")

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(comparison["ModelName"], comparison["F1 Score"])
ax.set_ylabel("F1 Score")
plt.xticks(rotation=25)

st.pyplot(fig)

# -----------------------------
# ROC Curve
# -----------------------------
st.subheader("ROC Curve")

st.image(
    "assets/roc_curve.png",
    use_container_width=True
)

# -----------------------------
# Precision Recall Curve
# -----------------------------
st.subheader("Precision-Recall Curve")

st.image(
    "assets/pr_curve.png",
    use_container_width=True
)

# -----------------------------
# Best Model
# -----------------------------
best_model = comparison.sort_values(
    by="F1 Score",
    ascending=False
).iloc[0]

st.success(
    f"""
🏆 Best Performing Model

Model : {best_model['ModelName']}

F1 Score : {best_model['F1 Score']:.4f}

Accuracy : {best_model['Accuracy']:.4f}
"""
)
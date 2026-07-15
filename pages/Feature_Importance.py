import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Feature Importance",
    page_icon="🌲",
    layout="wide"
)

st.title("🌲 Feature Importance")

st.write(
    "Understand which features contribute the most to fraud detection using the Random Forest model."
)

st.markdown("---")

st.subheader("Why Feature Importance?")

st.info("""
Random Forest estimates how much each feature contributes to the prediction.

Higher importance indicates a stronger influence on detecting fraudulent transactions.
""")

st.markdown("---")

st.subheader("Top 10 Important Features")

st.image(
    "assets/feature_importance.png",
    use_container_width=True
)

st.markdown("---")

st.subheader("Feature Importance Scores")

importance = pd.read_csv("assets/feature_importance.csv")

st.dataframe(
    importance,
    use_container_width=True
)

st.markdown("---")

st.subheader("Insights")

st.success("""
✔ Random Forest automatically ranks the most informative features.

✔ The top-ranked variables contribute the most toward identifying fraudulent transactions.

✔ Feature importance improves model interpretability without reducing prediction performance.

✔ PCA-transformed features (V1–V28) capture hidden transaction patterns used for fraud detection.
""")

st.markdown("---")

st.subheader("Why Random Forest?")

col1, col2 = st.columns(2)

with col1:
    st.metric("Accuracy", "99.95%")
    st.metric("F1 Score", "0.8482")

with col2:
    st.metric("Precision", "0.8710")
    st.metric("Recall", "0.8265")
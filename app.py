import streamlit as st
from predict import predict_transaction

st.set_page_config(
    page_title = "Credit Card Fraud Detection",
    page_icon = "💳",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

st.set_page_config(
    page_title = "Credit Card Fraud Detection",
    page_icon = "💳",
    layout = "wide"
)

st.title("💳 Credit Card Fraud Detection Web")
st.write("Enter the transaction details below to predict whether the transaction is Fraudulent or Legitimate.")

st.markdown("---")

st.subheader("Transaction Details")

features = []

col1, col2 = st.columns(2)

with col1:
    time = st.number_input("Time", value = 0.0)
    amount = st.number_input("Amount", value = 0.0)

features.append(time)

for i in range(1, 15):
    with col1:
        value = st.number_input(f"V{i}", value = 0.0, key = f"v{i}")
    features.append(value)

for i in range(15, 29):
    with col2:
        value = st.number_input(f"V{i}", value = 0.0, key = f"v{i}")
    features.append(value)

features.insert(1, amount)

st.markdown("---")

if st.button("Predict Transaction", use_container_width = True):

    prediction, confidence, fraud_probability = predict_transaction(features)

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")

    st.metric("Confidence", f"{confidence:.2f}%")
    st.metric("Fraud Probability", f"{fraud_probability:.2f}%")
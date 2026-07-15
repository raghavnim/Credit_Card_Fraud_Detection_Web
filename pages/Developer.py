import streamlit as st

st.set_page_config(
    page_title="Developer",
    page_icon="👨‍💻",
    layout="wide"
)

st.title("👨‍💻 Developer")

st.write(
    "Meet the developer behind the Credit Card Fraud Detection platform."
)

st.markdown("---")

# ==========================================================
# Profile
# ==========================================================

col1, col2 = st.columns([1,3])

with col1:
    st.image(
        "https://via.placeholder.com/220x220.png?text=Profile",
        width=220
    )

with col2:

    st.header("Raghav Nimgaonkar")

    st.write("""
Computer Science & Engineering Student

Visvesvaraya National Institute of Technology (VNIT), Nagpur
""")

    st.success("""
Machine Learning

Deep Learning

Data Analytics

Software Development
""")

st.markdown("---")

# ==========================================================
# Technical Skills
# ==========================================================

st.header("Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Programming")

    st.markdown("""
- Python
- C++
- SQL
""")

with col2:

    st.subheader("Machine Learning")

    st.markdown("""
- Scikit-Learn
- TensorFlow
- XGBoost
- Random Forest
- SMOTE
""")

with col3:

    st.subheader("Tools")

    st.markdown("""
- Streamlit
- Git
- GitHub
- VS Code
- Jupyter Notebook
""")

st.markdown("---")

# ==========================================================
# Project Highlights
# ==========================================================

st.header("Highlights")

st.info("""
✔ End-to-End Machine Learning Pipeline

✔ Interactive Streamlit Dashboard

✔ Seven ML/DL Models Evaluated

✔ Random Forest Deployment

✔ Model Performance Comparison

✔ Feature Importance Analysis

✔ ROC & Precision-Recall Evaluation
""")

st.markdown("---")

# ==========================================================
# Contact
# ==========================================================

st.header("Connect")

col1, col2 = st.columns(2)

with col1:
    st.write("**GitHub**")
    st.write("Add your GitHub profile link here")

with col2:
    st.write("**LinkedIn**")
    st.write("Add your LinkedIn profile link here")

st.markdown("---")

st.caption(
    "Built using Python • Streamlit • Scikit-Learn • TensorFlow"
)
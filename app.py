"""
app.py

Streamlit dashboard for CredifyAI.
Provides real-time credit risk inference using a trained ML model.

This app:
- Accepts borrower financial inputs
- Loads a persisted ML model
- Displays High Risk probability and classification

No training occurs here.
"""

import streamlit as st
from src.inference import predict_risk

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="CredifyAI – Credit Risk Dashboard",
    layout="centered"
)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("🚀 CredifyAI – Credit Risk Assessment")
st.write(
    "Enter borrower financial details to assess the **probability of High Credit Risk**."
)

st.markdown("---")

# -------------------------------------------------
# Input Section
# -------------------------------------------------

st.subheader("📥 Borrower Financial Inputs")

dti = st.number_input(
    "Debt-to-Income (DTI)",
    min_value=0.0,
    max_value=100.0,
    value=20.0,
    help="Total debt obligations as a percentage of income"
)

credit_utilization = st.number_input(
    "Credit Utilization (%)",
    min_value=0.0,
    max_value=100.0,
    value=30.0,
    help="Percentage of available credit currently being used"
)

emi_to_income = st.number_input(
    "EMI-to-Income Ratio",
    min_value=0.0,
    max_value=1.0,
    value=0.30,
    help="Monthly EMI burden relative to income"
)

loan_to_income = st.number_input(
    "Loan-to-Income Ratio",
    min_value=0.0,
    value=2.0,
    help="Total loan exposure relative to income"
)

active_loan_count = st.number_input(
    "Active Loan Count",
    min_value=0,
    step=1,
    value=1,
    help="Number of currently active loans"
)

delinquency_count = st.number_input(
    "Delinquency Count",
    min_value=0,
    step=1,
    value=0,
    help="Past delinquency occurrences"
)

# -------------------------------------------------
# Prediction Section
# -------------------------------------------------

st.markdown("---")

if st.button("🔍 Predict Credit Risk"):
    input_features = {
        "dti": dti,
        "credit_utilization": credit_utilization,
        "emi_to_income": emi_to_income,
        "loan_to_income": loan_to_income,
        "active_loan_count": active_loan_count,
        "delinquency_count": delinquency_count
    }

    try:
        result = predict_risk(input_features)

        st.subheader("📊 Prediction Result")

        if result["risk_label"] == "High Risk":
            st.error("⚠️ High Credit Risk Detected")
        else:
            st.success("✅ Not High Risk")

        st.metric(
            label="Probability of High Risk",
            value=f"{result['probability_high_risk'] * 100:.2f}%"
        )

        st.caption(f"Threshold used: {result['threshold_used']}")

    except Exception as e:
        st.error(f"Error during prediction: {e}")

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.markdown("---")
st.caption("CredifyAI • End-to-End Explainable Credit Risk System")

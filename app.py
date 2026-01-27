"""
app.py

Streamlit dashboard for CredifyAI.

This application provides:
- Real-time credit risk assessment
- Probability-based risk interpretation
- Human-readable explanations for decisions

IMPORTANT:
- No model training occurs here
- This app only performs inference using a persisted model
"""

import streamlit as st

from src.inference import predict_risk
from src.field_explanations import FIELD_EXPLANATIONS

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="CredifyAI – Credit Risk Dashboard",
    layout="centered"
)

# -------------------------------------------------
# Session State Initialization
# -------------------------------------------------
# Streamlit re-runs the script on every interaction.
# We store prediction results in session_state to
# persist them across reruns.

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("🚀 CredifyAI – Credit Risk Assessment")
st.write(
    "Enter borrower financial details to assess the "
    "**probability of High Credit Risk**."
)

st.markdown("---")

# -------------------------------------------------
# Input Section
# -------------------------------------------------

st.subheader("📥 Borrower Financial Inputs")

# Debt-to-Income
dti = st.number_input(
    FIELD_EXPLANATIONS["dti"]["label"],
    min_value=0.0,
    max_value=100.0,
    value=20.0,
    help=(
        f"{FIELD_EXPLANATIONS['dti']['description']} "
        f"{FIELD_EXPLANATIONS['dti']['why_it_matters']} "
        f"Healthy range: {FIELD_EXPLANATIONS['dti']['healthy_range']}."
    )
)

# Credit Utilization
credit_utilization = st.number_input(
    FIELD_EXPLANATIONS["credit_utilization"]["label"],
    min_value=0.0,
    max_value=100.0,
    value=30.0,
    help=(
        f"{FIELD_EXPLANATIONS['credit_utilization']['description']} "
        f"{FIELD_EXPLANATIONS['credit_utilization']['why_it_matters']} "
        f"Healthy range: {FIELD_EXPLANATIONS['credit_utilization']['healthy_range']}."
    )
)

# EMI-to-Income
emi_to_income = st.number_input(
    FIELD_EXPLANATIONS["emi_to_income"]["label"],
    min_value=0.0,
    max_value=1.0,
    value=0.30,
    help=(
        f"{FIELD_EXPLANATIONS['emi_to_income']['description']} "
        f"{FIELD_EXPLANATIONS['emi_to_income']['why_it_matters']} "
        f"Healthy range: {FIELD_EXPLANATIONS['emi_to_income']['healthy_range']}."
    )
)

# Loan-to-Income
loan_to_income = st.number_input(
    FIELD_EXPLANATIONS["loan_to_income"]["label"],
    min_value=0.0,
    value=2.0,
    help=(
        f"{FIELD_EXPLANATIONS['loan_to_income']['description']} "
        f"{FIELD_EXPLANATIONS['loan_to_income']['why_it_matters']} "
        f"Healthy range: {FIELD_EXPLANATIONS['loan_to_income']['healthy_range']}."
    )
)

# Active Loans
active_loan_count = st.number_input(
    FIELD_EXPLANATIONS["active_loan_count"]["label"],
    min_value=0,
    step=1,
    value=1,
    help=(
        f"{FIELD_EXPLANATIONS['active_loan_count']['description']} "
        f"{FIELD_EXPLANATIONS['active_loan_count']['why_it_matters']}."
    )
)

# Delinquency Count
delinquency_count = st.number_input(
    FIELD_EXPLANATIONS["delinquency_count"]["label"],
    min_value=0,
    step=1,
    value=0,
    help=(
        f"{FIELD_EXPLANATIONS['delinquency_count']['description']} "
        f"{FIELD_EXPLANATIONS['delinquency_count']['why_it_matters']}."
    )
)

# -------------------------------------------------
# Prediction Trigger
# -------------------------------------------------

st.markdown("---")

if st.button("🔍 Predict Credit Risk"):
    input_features = {
        "dti": dti,
        "credit_utilization": credit_utilization,
        "emi_to_income": emi_to_income,
        "loan_to_income": loan_to_income,
        "active_loan_count": active_loan_count,
        "delinquency_count": delinquency_count,
    }

    try:
        # Run inference and store result in session state
        st.session_state.prediction_result = predict_risk(input_features)

    except Exception as exc:
        st.error(f"Prediction failed: {exc}")
        st.session_state.prediction_result = None

# -------------------------------------------------
# Prediction Output
# -------------------------------------------------

result = st.session_state.prediction_result

if result is not None:
    st.subheader("📊 Risk Assessment Result")

    # Risk band display
    if result["risk_band"] == "High Risk":
        st.error("⚠️ High Risk")
    elif "Medium" in result["risk_band"]:
        st.warning("⚠️ Medium Risk (Watchlist)")
    else:
        st.success("✅ Low Risk")

    # Probability metric
    st.metric(
        label="Probability of High Risk",
        value=f"{result['probability_high_risk'] * 100:.2f}%"
    )

    # Decision guidance
    st.write(f"**Decision Guidance:** {result['decision']}")

    # -------------------------------------------------
    # Human-Readable Risk Reasons
    # -------------------------------------------------

    st.subheader("🧠 Key Risk Drivers")

    for reason in result["key_reasons"]:
        st.write(f"• {reason}")

# -------------------------------------------------
# Footer & Disclaimer
# -------------------------------------------------

st.markdown("---")
st.caption("CredifyAI • End-to-End Explainable Credit Risk System")

st.info(
    "ℹ️ This output represents a statistical estimate based on historical data. "
    "It does not guarantee future outcomes and should be combined with policy "
    "rules and human review."
)

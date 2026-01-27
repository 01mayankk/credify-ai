"""
risk_reasons.py

Human-readable risk explanation rules for CredifyAI.
"""

def generate_risk_reasons(features: dict):
    """
    Generate plain-English reasons explaining risk outcome.
    """

    reasons = []

    # EMI-to-Income
    if features["emi_to_income"] > 0.5:
        reasons.append("A large portion of income goes toward monthly EMIs")

    # Loan-to-Income
    if features["loan_to_income"] > 3:
        reasons.append("Total loan exposure is high relative to income")

    # Credit Utilization
    if features["credit_utilization"] > 70:
        reasons.append("Most available credit is already being used")

    # Debt-to-Income
    if features["dti"] > 40:
        reasons.append("Overall debt obligations consume a large share of income")

    # Delinquency History
    if features["delinquency_count"] > 0:
        reasons.append("Past delays or missed payments are on record")

    # Active Loans
    if features["active_loan_count"] > 3:
        reasons.append("Multiple active loans increase repayment complexity")

    if not reasons:
        reasons.append("No major risk indicators detected")

    return reasons

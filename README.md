# 🚀 CredifyAI — End-to-End Explainable Credit Risk System

CredifyAI is an end-to-end machine learning system for **probability-based credit risk assessment** using structured financial data.

It covers the full ML lifecycle — from raw data ingestion and feature engineering to model training, explainability, inference, and an interactive dashboard.

⚠️ **Important:**  
CredifyAI predicts the **probability of a borrower being High Risk** based on historical outcomes.  
Final credit decisions should be made by applying policy thresholds on top of model outputs.

---

## 🎯 Project Objective

To build a **transparent and defensible** credit risk model that:

- Learns meaningful financial patterns (not hard-coded rules)
- Handles class imbalance realistically
- Provides interpretable explanations
- Can be used for real-time risk scoring

---

## 🧠 Core Problem

Traditional credit scoring systems often rely on:

- Static rules
- Hard thresholds
- Opaque decision logic

**CredifyAI replaces this** with a probability-based ML approach that allows:

- Risk ranking instead of binary judgment
- Post-model policy control
- Explainable predictions using SHAP

---

## 📊 Dataset

- **Source:** LendingClub Loan Dataset (2007–2015)
- **Size:** ~2.2 million records
- **Type:** Structured financial + repayment data
- **Note:** Raw data is excluded from the repository due to size and licensing

---

## 🏗️ Project Architecture

```
credify-ai/
├── app.py                    # Streamlit dashboard (UI)
├── src/
│   ├── preprocess.py         # Data cleaning & validation
│   ├── features.py           # Feature engineering (6 core features)
│   ├── train_model.py        # Model training & evaluation
│   ├── explain.py            # SHAP explainability utilities
│   ├── inference.py          # Inference-only pipeline
│   └── model_io.py           # Model save/load utilities
├── scripts/
│   ├── save_model.py         # Train & persist final model
│   ├── test_inference.py     # Inference sanity check
│   ├── verify_preprocessing.py
│   ├── verify_features.py
│   ├── verify_train_model.py
│   └── verify_explainability.py
├── visuals/
│   └── shap_summary_high_risk.png
├── models/                   # Saved model artifacts (gitignored)
├── data/                     # Raw & processed data (gitignored)
│   ├── raw/
│   └── processed/
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔑 Feature Set (Deliberately Minimal)

The model uses **6 defensible financial features**:

1. **emi_to_income** — Monthly repayment burden relative to income
2. **loan_to_income** — Loan exposure relative to earning capacity
3. **credit_utilization** — Percentage of revolving credit already used
4. **dti** — Debt-to-Income ratio (overall debt stress)
5. **active_loan_count** — Number of current open loans
6. **delinquency_count** — Past repayment failures (behavioral signal)

**Feature count is intentionally constrained** to reduce noise and improve interpretability.

---

## ✅ Phase 1: Data Ingestion & Preprocessing (Completed)

This phase establishes a robust and auditable preprocessing pipeline.

### What's Implemented

- Safe loading of large CSV datasets
- Strict column whitelisting (schema enforcement)
- Finance-aligned missing value handling
- Removal of invalid financial records
- Business-driven credit risk label creation
- End-to-end preprocessing verification script

### Risk Labels

- **Low Risk**
- **Moderate Risk**
- **High Risk**

### Verification

```bash
python scripts/verify_preprocessing.py
```

---

## ✅ Phase 2: Feature Engineering (Completed)

This phase converts cleaned financial data into a compact, high-signal feature set.

### Design Principles

- Minimal and non-redundant feature set
- Ratios instead of raw monetary values
- High interpretability for stakeholders and explainability tools
- Avoidance of correlated or redundant signals

### Verification

```bash
python scripts/verify_features.py
```

---

## ✅ Phase 3: Model Training & Evaluation (Completed)

### 🤖 Model Details

- **Algorithm:** XGBoost
- **Formulation:** Binary (High Risk vs Rest)
- **Output:** Probability of High Risk
- **Imbalance Handling:** Class-balanced training
- **Persistence:** Saved using joblib

### Evaluation Metrics

- **Primary Focus:** Recall for High Risk class (minimize false negatives)
- **Secondary Metrics:** Precision, F1-score for balanced assessment
- **Error Analysis:** Confusion matrix for misclassification patterns

### Verification

```bash
python scripts/verify_train_model.py
```

---

## ✅ Phase 4: Model Explainability (Completed)

### 📈 SHAP-Based Explainability

CredifyAI uses **SHAP** (SHapley Additive exPlanations) to explain model behavior.

### Global Explainability

- Identifies strongest drivers of high-risk predictions
- Confirms alignment with financial intuition
- Avoids leakage and spurious correlations

### Primary Risk Drivers Observed

1. EMI-to-Income ratio
2. Loan-to-Income ratio
3. Credit utilization
4. Delinquency history

📷 **SHAP summary plot is saved in:**  
`visuals/shap_summary_high_risk.png`

### Why This Matters

This phase validates that the model learns **financially meaningful patterns**, not spurious correlations. The explainability outputs ensure:

- Regulatory compliance and audit readiness
- Stakeholder trust in model decisions
- Identification of key risk drivers
- Validation of domain knowledge alignment

### Verification

```bash
python scripts/verify_explainability.py
```

---

## ✅ Phase 5: Inference Pipeline (Completed)

### 🧪 Inference Details

Inference is **fully decoupled** from training.

- Loads persisted model
- Validates feature schema
- Produces deterministic predictions
- Designed for reuse by UI / CLI / APIs

### Example Output

```json
{
  "risk_label": "Not High Risk",
  "probability_high_risk": 0.0695,
  "threshold_used": 0.5
}
```

### Test Inference

```bash
python scripts/test_inference.py
```

---

## ✅ Phase 6: Interactive Dashboard (Completed)

### 🖥️ Streamlit Dashboard

CredifyAI includes a **Streamlit dashboard** for real-time inference.

### Features

- Manual borrower input via user-friendly form
- Instant risk prediction
- Probability-based output (not binary)
- Clean, audit-friendly UI
- SHAP summary visualization

### Run Locally

```bash
streamlit run app.py
```

### ⚠️ Important Design Note (Intentional)

CredifyAI does **NOT** enforce approval or rejection rules.

It returns a **risk probability**, allowing downstream systems to:

- Apply risk bands
- Define rejection thresholds
- Implement policy overlays

**This separation reflects real banking architectures.**

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn, XGBoost
- **Explainability:** SHAP
- **Visualization:** Matplotlib, Seaborn
- **Dashboard:** Streamlit
- **Model Persistence:** Joblib
- **Workflow:** Modular ML pipeline with verification scripts

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Run Complete Pipeline

```bash
# Step 1: Preprocess raw data
python scripts/verify_preprocessing.py

# Step 2: Engineer features
python scripts/verify_features.py

# Step 3: Train and evaluate model
python scripts/verify_train_model.py

# Step 4: Generate SHAP explanations
python scripts/verify_explainability.py

# Step 5: Save trained model for inference
python scripts/save_model.py

# Step 6: Test inference pipeline
python scripts/test_inference.py

# Step 7: Launch interactive dashboard
streamlit run app.py
```

---

## 🧠 Learning Outcomes

This project demonstrates:

- End-to-end ML pipeline design
- Feature engineering for finance
- Class imbalance handling
- Explainable ML (SHAP)
- Model persistence & inference
- ML dashboards using Streamlit
- Production-style project structure
- Separation of model logic and business rules

---

## 🚧 Future Enhancements (Optional)

- Risk banding (Low / Watchlist / High)
- Adjustable decision thresholds in UI
- Per-borrower SHAP explanations in dashboard
- REST API via FastAPI
- Model monitoring and drift detection
- Deployment (Streamlit Cloud / HuggingFace Spaces)
- A/B testing framework

---

## 👤 Author

**Mayank Kumar**  
GitHub: [https://github.com/01mayankk](https://github.com/01mayankk)

---

## 📌 Project Philosophy

Each phase is completed, verified, and committed independently to ensure:

- **Reproducibility:** Clear verification scripts for every stage
- **Interpretability:** Financial domain alignment in features and evaluation
- **Maintainability:** Modular codebase with separation of concerns
- **Production-readiness:** Industry-standard practices from day one
- **Transparency:** Probability-based outputs, not black-box decisions

---

## 📄 License

This project is released under the MIT License.

---

**Current Status:** All Phases Complete ✅ | Production-Ready ML System
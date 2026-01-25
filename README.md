# 🚀 CredifyAI – Credit Risk Classification System

CredifyAI is an end-to-end machine learning project focused on building an **interpretable and production-ready credit risk classification system** using structured financial data.

The project is developed **phase by phase**, with each stage fully validated, version-controlled, and reproducible, following real-world ML engineering practices.

---

## 📌 Project Objective

To classify loan applicants into **Low**, **Moderate**, or **High** credit risk categories using a small, defensible set of financial indicators that align with real-world credit risk assessment principles.

---

## 📊 Dataset

- **Source:** LendingClub Loan Dataset (2007–2015)
- **Scale:** ~2.2 million records
- **Type:** Structured financial and repayment data
- **Note:**  
  Raw data is **not included** in this repository due to size and licensing constraints.  
  Users must download the dataset separately and place it under `data/raw/`.

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

Run the preprocessing verification script:
```bash
python scripts/verify_preprocessing.py
```

This script validates:

- Dataset loading
- Schema enforcement
- Cleaning logic
- Target label creation
- Final dataset shape and class distribution

---

## ✅ Phase 2: Feature Engineering (Completed)

This phase converts cleaned financial data into a compact, high-signal feature set suitable for ML modeling.

### Engineered Features (6 Core Signals)

1. **Debt-to-Income (DTI)**  
   Measures overall debt stress from existing obligations.

2. **Credit Utilization**  
   Indicates how much revolving credit is already being used.

3. **EMI-to-Income Ratio**  
   Captures monthly repayment burden relative to income.

4. **Loan-to-Income Ratio**  
   Measures loan exposure relative to earning capacity.

5. **Active Loan Count**  
   Represents financial complexity and credit exposure.

6. **Delinquency Count**  
   Encodes past repayment failures (strong behavioral signal).

### Design Principles

- Minimal and non-redundant feature set
- Ratios instead of raw monetary values
- High interpretability for stakeholders and explainability tools
- Avoidance of correlated or redundant signals

### Verification

Run the feature engineering verification script:
```bash
python scripts/verify_features.py
```

This script validates:

- Feature schema contract
- Absence of missing values
- Correct target distribution
- Sample feature sanity checks

---

## 🗂️ Project Structure
```
credify-ai/
├── src/
│   ├── preprocess.py          # Data ingestion & cleaning
│   └── features.py             # Feature engineering
├── scripts/
│   ├── verify_preprocessing.py
│   └── verify_features.py
├── data/
│   ├── raw/                    # ignored by git
│   └── processed/              # ignored by git
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack (Current Phases)

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Workflow:** Modular pipeline with verification scripts

---

## 🚧 Upcoming Phases

- Model training with XGBoost
- Handling class imbalance
- Model evaluation using recall, precision, and F1-score
- Explainability using SHAP
- Deployment-ready scoring pipeline

---

## 👤 Author

**Mayank Kumar**  
GitHub: [https://github.com/01mayankk](https://github.com/01mayankk)

---

## 📌 Project Philosophy

Each phase is completed, verified, and committed independently to ensure reproducibility, interpretability, and long-term maintainability.
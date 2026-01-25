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

## ✅ Phase 3: Model Training & Evaluation (Completed)

This phase implements a production-grade classification model with robust evaluation metrics.

### Model Architecture

- **Algorithm:** XGBoost (multiclass classification)
- **Imbalance Handling:** Class-weighted loss function
- **Data Split:** Stratified train/validation split
- **Optimization:** Grid search for hyperparameter tuning (optional)

### Evaluation Metrics

- **Primary Focus:** Recall for High and Moderate risk classes (minimize false negatives)
- **Secondary Metrics:** Precision, F1-score for balanced assessment
- **Error Analysis:** Confusion matrix for misclassification patterns
- **Class-wise Performance:** Per-class precision, recall, and F1-score

### Verification

Run the model training verification script:
```bash
python scripts/verify_train_model.py
```

This script:

- Trains the XGBoost model with class weighting
- Performs stratified train/validation split
- Evaluates using precision, recall, and F1-score
- Generates confusion matrix for error analysis
- Outputs classification report with per-class metrics

---

## 🗂️ Project Structure

```
credify-ai/
├── src/
│   ├── preprocess.py           # Data ingestion & cleaning
│   ├── features.py              # Feature engineering
│   ├── train_model.py           # Model training pipeline
│   └── evaluate.py              # Evaluation metrics & analysis
├── scripts/
│   ├── verify_preprocessing.py
│   ├── verify_features.py
│   └── verify_train_model.py
├── data/
│   ├── raw/                     # ignored by git
│   └── processed/               # ignored by git
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn, XGBoost
- **Evaluation:** Scikit-learn metrics
- **Workflow:** Modular ML pipeline with verification scripts

---

## 🚧 Upcoming Phases

### Phase 4: Model Explainability (Next)

- SHAP (SHapley Additive exPlanations) integration
- Feature attribution analysis
- Risk reasoning validation
- Verification of financial logic learned by the model
- Individual prediction explanations

### Phase 5: Deployment Pipeline (Future)

- Model serialization and versioning
- REST API for real-time scoring
- Batch prediction pipeline
- Model monitoring and drift detection

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
```

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

---

## 📄 License

This project is available for educational and portfolio purposes.

---

**Current Status:** Phase 3 Complete ✅ | Next: Model Explainability with SHAP
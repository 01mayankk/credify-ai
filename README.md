# 🚀 CredifyAI – Credit Risk Classification System

CredifyAI is an end-to-end machine learning project focused on building an interpretable credit risk classification system using structured financial data.

This repository currently contains **Phase 1: Data Ingestion & Preprocessing**, implemented with production-style practices and validation scripts.

---

## 📌 Project Objective
To classify loan applicants into **Low**, **Moderate**, or **High** credit risk categories using clean, defensible financial indicators.

---

## 📊 Dataset
- Source: LendingClub Loan Dataset (2007–2015)
- Rows: ~2.2 million
- Note: Raw data is not included in the repository due to size and licensing.

---

## ✅ Phase 1: Data Preprocessing (Completed)

### What’s implemented:
- Safe loading of large CSV datasets
- Strict column whitelisting (schema enforcement)
- Finance-aligned data cleaning
- Interpretable risk label creation
- End-to-end preprocessing verification script

### Final Target Distribution:
- Low Risk
- Moderate Risk
- High Risk

---

## 🗂️ Project Structure
```
credify-ai/
├── src/
│ └── preprocess.py
├── scripts/
│ └── verify_preprocessing.py
├── data/
│ ├── raw/ # ignored by git
│ └── processed/ # ignored by git
├── requirements.txt
├── README.md
└── .gitignore

```
---

## ▶️ How to Verify Preprocessing

Run the verification script from the project root:

```bash
python scripts/verify_preprocessing.py

This will:

Load the dataset

Validate schema

Clean invalid records

Generate risk labels

Print final dataset shape and class distribution

🛠️ Tech Stack (Current Phase)

Python

Pandas

NumPy

🚧 Upcoming Phases

Feature engineering (6 core financial features)

Model training (XGBoost)

Model evaluation & explainability (SHAP)

Deployment-ready scoring pipeline

👤 Author

Mayank Kumar
GitHub: https://github.com/01mayankk

```
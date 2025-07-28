# 🧪 Data Quality Framework

A scalable, modular data quality framework built using Python, Pandas, Great Expectations, and Deequ. This tool automates data validation, profiling, and dashboarding for any CSV-based dataset.

## 🚀 Features
- Schema validation
- Null & duplicate detection
- Cardinality and entropy profiling
- Outlier detection
- Label normalization and NLP-based cleaning
- Power BI dashboard-ready output

## ⚙️ Tech Stack
- Python, Pandas
- Great Expectations, Deequ
- Power BI
- Streamlit (optional)

## 📁 Structure
```
data/
  └── sample.csv
notebooks/
  └── EDA.ipynb
src/
  ├── preprocessing.py
  ├── validation.py
  └── profiling.py
app/
  └── app.py
```

## 🔧 How to Run
1. Place your CSV file in the `data/` directory.
2. Run `python src/preprocessing.py`
3. Run `python src/validation.py`
4. Run `python src/profiling.py`
5. Output results can be visualized via Power BI or Streamlit (coming soon)

## 🧠 Future Work
- Streamlit dashboard UI
- Cloud-based deployment with Azure
- Email alert system for data quality failures

---
Made by James Venkatesan

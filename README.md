# Data Quality Framework

A scalable, modular data quality framework built using Python, Pandas, Great Expectations, and Deequ. This tool automates data validation, profiling, and dashboarding for any CSV-based dataset.

## Features
- Schema validation
- Null & duplicate detection
- Cardinality and entropy profiling
- Outlier detection
- Label normalization and NLP-based cleaning
- Power BI dashboard-ready output

## Tech Stack
- Python, Pandas
- Great Expectations, Deequ
- Power BI
- Streamlit 

## Structure
```
requriements.txt
data/
  └── sample.csv
src/
  ├── preprocessing.py
  ├── validation.py
  └── profiling.py
app/
  └── app.py
```

## How to Run
1. Clone Repo to your PC
2. Open terminal and navigate to current file path
3. Make sure you have everything needed `pip install -r requirements.txt`
4. Run `streamlit run app/app.py`

## Future Work
- Streamlit dashboard UI
- Cloud-based deployment with Azure
- Email alert system for data quality failures

---
Made by James Venkatesan

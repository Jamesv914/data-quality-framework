# Data Quality Framework

A scalable, modular data quality framework built using Python, Pandas, and Streamlit — with planned support for Great Expectations and Deequ. This tool automates data validation, profiling, and interactive dashboarding for any CSV-based dataset.

## Features
	•	Schema validation (planned with Great Expectations)
	•	Null & duplicate detection
	•	Cardinality and entropy profiling (coming soon)
	•	Outlier detection (planned)
	•	Label normalization and NLP-based cleaning (planned)
	•	Interactive Streamlit dashboard with:
	•	Null value summary + bar chart
	•	Correlation heatmap
	•	Column statistics explorer
	•	Automated Data Quality Scoreboard
	•	Power BI export-ready output

⸻

## Tech Stack
	•	Python, Pandas
	•	Matplotlib, Seaborn
	•	Streamlit
	•	(Optional/Planned): Great Expectations, Deequ
	•	Power BI (for external visualization)

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
- Cloud-based deployment
- Email alert system for data quality failures

---
Made by James Venkatesan

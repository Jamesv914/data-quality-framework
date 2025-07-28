import streamlit as st
import pandas as pd

st.title("📊 Data Quality Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.dataframe(df.head())

    st.write("Null Values:")
    st.write(df.isnull().sum())

    st.write("Duplicate Rows:", df.duplicated().sum())

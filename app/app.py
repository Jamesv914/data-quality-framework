import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Quality Dashboard", layout="wide")
st.title("Data Quality Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head(10))

    st.subheader("Null Values")
    null_counts = df.isnull().sum()
    st.dataframe(null_counts[null_counts > 0])

    st.markdown("### Duplicate Rows")
    st.write(df.duplicated().sum())

    # Null bar chart
    st.subheader("Nulls per Column (Bar Chart)")
    if null_counts.sum() > 0:
        fig, ax = plt.subplots()
        null_counts[null_counts > 0].sort_values(ascending=False).plot(kind='bar', ax=ax, color='tomato')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)
    else:
        st.success("No nulls detected!")

    # Correlation heatmap
    st.subheader("Correlation Heatmap (Numeric Columns)")
    numeric_df = df.select_dtypes(include='number')
    if not numeric_df.empty:
        fig, ax = plt.subplots()
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.info("No numeric columns available for correlation analysis.")

    # Column summary selector
    st.subheader("🔍 Column Summary Explorer")
    column = st.selectbox("Choose a column to explore", df.columns)
    st.write("📌 Basic statistics:")
    st.write(df[column].describe())
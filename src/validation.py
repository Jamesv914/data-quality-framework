import pandas as pd

def check_nulls(df):
    print("Null value count per column:")
    print(df.isnull().sum())

def check_duplicates(df):
    print(f"Total duplicate rows: {df.duplicated().sum()}")

if __name__ == "__main__":
    df = pd.read_csv("data/sample.csv")
    check_nulls(df)
    check_duplicates(df)

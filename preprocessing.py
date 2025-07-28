import pandas as pd

def load_data(path):
    print(f"Loading data from {path}")
    return pd.read_csv(path)

def basic_cleaning(df):
    print("Running basic cleaning...")
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

if __name__ == "__main__":
    df = load_data("data/sample.csv")
    df = basic_cleaning(df)
    print(df.head())

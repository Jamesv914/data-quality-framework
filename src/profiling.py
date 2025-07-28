import pandas as pd
import numpy as np

def profile_cardinality(df):
    print("Cardinality of each column:")
    print(df.nunique())

def profile_entropy(df):
    print("Entropy analysis:")
    for col in df.select_dtypes(include='object'):
        probs = df[col].value_counts(normalize=True)
        entropy = -np.sum(probs * np.log2(probs))
        print(f"{col}: {entropy:.4f}")

if __name__ == "__main__":
    df = pd.read_csv("data/sample.csv")
    profile_cardinality(df)
    profile_entropy(df)

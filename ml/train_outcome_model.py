import pandas as pd

df = pd.read_csv("datasets/patient_outcomes.csv")

print("Columns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
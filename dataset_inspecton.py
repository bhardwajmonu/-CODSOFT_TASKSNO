import pandas as pd 

df = pd.read_csv("students.csv")
print("======DATASET INSPECTION======")

print("\nComplete Dataset:")
print(df)


print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\n========== INSPECTION COMPLETED ==========")

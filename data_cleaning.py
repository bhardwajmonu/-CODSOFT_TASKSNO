import pandas as pd
df = pd.read_csv("students.csv")
print("========== ORIGINAL DATASET ==========")
print(df)
print("\nDataset Shape:")
print(df.shape)
print("\nData Types:")
print(df.dtypes)
print("\nDataset Information:")
df.info()
print("\n========== MISSING VALUES ==========")
missing_values = df.isnull().sum()
print(missing_values)
print("\n========== DUPLICATE RECORDS ==========")
print("Number of duplicates:", df.duplicated().sum())
print("\nDuplicate rows:")
print(df[df.duplicated()])
print("\n========== UNIQUE VALUES ==========")

for column in df.select_dtypes(include="object").columns:
    print(f"\n{column}:")
    print(df[column].unique())

text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.strip()
if "Gender" in df.columns:
    df["Gender"] = df["Gender"].str.lower()
    df["Gender"] = df["Gender"].replace({
        "male": "Male",
        "female": "Female"
    })    
if "Course" in df.columns:
    df["Course"] = df["Course"].str.title()   
if "City" in df.columns:
    df["City"] = df["City"].str.title()
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
df = df.drop_duplicates()
df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(int)
print("\n========== CLEANED DATASET ==========")
print(df)
print("\nCleaned Dataset Shape:")
print(df.shape)
print("\nCleaned Data Types:")
print(df.dtypes)
print("\nRemaining Missing Values:")
print(df.isnull().sum())
print("\nRemaining Duplicate Records:")
print(df.duplicated().sum())
df.to_csv("output/cleaned_students.csv", index=False)

print("\n========================================")
print("Cleaned dataset saved successfully!")
print("File: output/cleaned_students.csv")
print("========================================")



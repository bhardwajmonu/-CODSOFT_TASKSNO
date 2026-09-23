import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# TASK 4: CUSTOMER ANALYSIS
# ==========================================

# Load customer dataset
df = pd.read_csv("customers.csv")

# Create output folder
os.makedirs("output", exist_ok=True)

sns.set_theme(style="whitegrid")

print("=" * 60)
print("TASK 4: CUSTOMER PURCHASING BEHAVIOR ANALYSIS")
print("=" * 60)

# 1. Basic Dataset Information

print("\n--- Dataset Information ---")

print("Number of Customers:", len(df))
print("Number of Features:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

# 2. Basic Statistics

print("\n--- Descriptive Statistics ---")

print(df.describe())

# 3. Customer Segmentation by Age

def age_group(age):
    if age < 25:
        return "18-24"
    elif age < 35:
        return "25-34"
    elif age < 45:
        return "35-44"
    else:
        return "45+"

df["AgeGroup"] = df["Age"].apply(age_group)

print("\n--- Customers by Age Group ---")
print(df["AgeGroup"].value_counts())

# 4. Customer Segmentation by Location
print("\n--- Customers by Location ---")

location_count = df["Location"].value_counts()

print(location_count)

# 5. Spending by Age Group
print("\n--- Spending by Age Group ---")

age_spending = df.groupby("AgeGroup")["TotalSpent"].agg(
    ["count", "mean", "sum"]
)

print(age_spending)

# 6. Spending by Location

print("\n--- Spending by Location ---")

location_spending = df.groupby("Location")["TotalSpent"].agg(
    ["count", "mean", "sum"]
)

print(location_spending)

# 7. Purchasing Frequency Analysis

print("\n--- Purchase Frequency Analysis ---")

print("Average Purchase Frequency:",
      round(df["PurchaseFrequency"].mean(), 2))

print("Maximum Purchase Frequency:",
      df["PurchaseFrequency"].max())

print("Minimum Purchase Frequency:",
      df["PurchaseFrequency"].min())

# 8. Identify Valuable Customers

print("\n--- Top Customers by Total Spending ---")

top_customers = df.sort_values(
    by="TotalSpent",
    ascending=False
).head(5)

print(
    top_customers[
        ["CustomerID", "Age", "Location",
         "PurchaseFrequency", "TotalSpent"]
    ]
)

# 9. Segment Customers by Spending
def spending_segment(amount):

    if amount < 10000:
        return "Low Value"

    elif amount < 25000:
        return "Medium Value"

    else:
        return "High Value"


df["SpendingSegment"] = df["TotalSpent"].apply(
    spending_segment
)

print("\n--- Spending Segments ---")

print(
    df["SpendingSegment"].value_counts()
)

# 10. Most Valuable Customer Group

segment_analysis = df.groupby(
    "SpendingSegment"
).agg(
    Customers=("CustomerID", "count"),
    Average_Spending=("TotalSpent", "mean"),
    Total_Revenue=("TotalSpent", "sum")
)

print("\n--- Customer Segment Analysis ---")
print(segment_analysis)

# 11. Relationship Between Purchases

correlation = df[
    ["Age", "PurchaseFrequency", "TotalSpent"]
].corr()

print("\n--- Correlation Analysis ---")
print(correlation)

# 12. Visualization 1
# Spending by Location
plt.figure(figsize=(8, 5))

location_spending["sum"].sort_values(
    ascending=False
).plot(kind="bar")

plt.title("Total Customer Spending by Location")
plt.xlabel("Location")
plt.ylabel("Total Spending")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "output/customer_spending_by_location.png"
)

plt.show()

# 13. Visualization 2
# Customer Spending Segments

plt.figure(figsize=(7, 7))

df["SpendingSegment"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Customer Spending Segments")
plt.ylabel("")

plt.tight_layout()

plt.savefig(
    "output/customer_spending_segments.png"
)

plt.show()

# 14. Visualization 3
# Age vs Total Spending
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Age",
    y="TotalSpent",
    hue="SpendingSegment",
    s=100
)

plt.title("Age vs Total Customer Spending")
plt.xlabel("Age")
plt.ylabel("Total Spending")

plt.tight_layout()

plt.savefig(
    "output/age_vs_spending.png"
)
plt.show()

# 15. Visualization 4
# Purchase Frequency vs Spending

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="PurchaseFrequency",
    y="TotalSpent",
    hue="Location",
    s=100
)

plt.title("Purchase Frequency vs Total Spending")
plt.xlabel("Purchase Frequency")
plt.ylabel("Total Spending")

plt.tight_layout()

plt.savefig(
    "output/purchase_frequency_vs_spending.png"
)
plt.show()

# 16. Marketing Insights

print("\n" + "=" * 60)
print("MARKETING INSIGHTS")
print("=" * 60)

print("""
1. High-value customers should receive loyalty rewards,
   exclusive offers, and personalized promotions.

2. Medium-value customers can be encouraged to increase
   their spending through bundles and targeted discounts.

3. Low-value customers can be targeted with introductory
   offers and promotional campaigns.

4. Locations with higher total spending can receive
   location-specific marketing campaigns.

5. Customers with high purchase frequency can be included
   in loyalty programs to encourage repeat purchases.

6. Purchase frequency and total spending can be analyzed
   together to identify highly engaged customers.
""")

# 17. Save Analysis Dataset
df.to_csv(
    "output/customer_analysis.csv",
    index=False
)

print("\nAnalysis completed successfully!")
print("Results saved in the output folder.")
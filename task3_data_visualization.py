import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# TASK 3: DATA VISUALIZATION


# Load dataset
df = pd.read_csv("students.csv")

# Create output directory
os.makedirs("output", exist_ok=True)

# Set Seaborn style
sns.set_theme(style="whitegrid")


# 1. BAR CHART
# Average Marks by Course


course_marks = df.groupby("Course")["Marks"].mean()

plt.figure(figsize=(8, 5))

plt.bar(course_marks.index, course_marks.values)

plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("Average Marks")

plt.tight_layout()
plt.savefig("output/bar_chart.png")
plt.show()

# 2. LINE CHART
# Student Marks


plt.figure(figsize=(10, 5))

plt.plot(
    df["Name"],
    df["Marks"],
    marker="o",
    linewidth=2
)

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("output/line_chart.png")
plt.show()

# 3. PIE CHART
# Students by course

course_count = df["Course"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    course_count.values,
    labels=course_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribution of Students by Course")

plt.tight_layout()
plt.savefig("output/pie_chart.png")
plt.show()

# 4. HISTOGRAM
# Distribution of Marks

plt.figure(figsize=(8, 5))

plt.hist(
    df["Marks"],
    bins=5,
    edgecolor="black"
)

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.savefig("output/histogram.png")
plt.show()

# 5. SCATTER PLOT
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Age",
    y="Marks",
    s=100
)

plt.title("Relationship Between Age and Marks")
plt.xlabel("Age")
plt.ylabel("Marks")

plt.tight_layout()
plt.savefig("output/scatter_plot.png")
plt.show()

# 6. PRINT INSIGHTS

print("\n" + "=" * 60)
print("DATA VISUALIZATION INSIGHTS")
print("=" * 60)

print("\n1. BAR CHART")
print("The bar chart compares the average marks of students across courses.")

print("\n2. LINE CHART")
print("The line chart shows the marks of individual students.")

print("\n3. PIE CHART")
print("The pie chart shows the proportion of students in each course.")

print("\n4. HISTOGRAM")
print("The histogram shows the distribution of student marks.")

print("\n5. SCATTER PLOT")
print("The scatter plot shows the relationship between age and marks.")

print("\nAll charts have been saved in the output folder.")

print("\nVisualization task completed successfully!")
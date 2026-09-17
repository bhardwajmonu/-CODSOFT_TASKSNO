import pandas as pd\
#load Dataset
df = pd.read_csv("data/students.csv")
print("=" * 60)
print("TASK 2: DESCRIPTIVE STATISTICS & DATA ANALYSIS")
print("=" * 60)

#Basic Data information
print("\n--- Dataset Shape ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types ---")
print(df.dtypes)

#Descriptive statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())

#Numeriacl Feature analysis
print("\n--- Numerical Feature Analysis ---")

numeric_columns = df.select_dtypes(include="number").columns
for column in numeric_columns:
    print(f"\n{column}")
    print("Mean:", df[column].mean())
    print("Median:", df[column].median())
    print("Minimum:", df[column].min())
    print("Maximum:", df[column].max())
    print("Standard Deviation:", df[column].std())

#Categorical feature analysis
print("\n--- Gender Distribution ---")
if "Gender" in df.columns:
    print(df["Gender"].value_counts())
print("\n--- Course Distribution ---")
if "Course" in df.columns:
    print(df["Course"].value_counts())
print("\n--- City Distribution ---")
if "City" in df.columns:
    print(df["City"].value_counts())

#relationship between variables
print("\n--- Correlation Between Numerical Variables ---")
correlation = df[numeric_columns].corr()
print(correlation)

#Average Marks by Course
if "Course" in df.columns and "Marks" in df.columns:
    print("\n--- Average Marks by Course ---")
    course_marks = df.groupby("Course")["Marks"].mean()
    print(course_marks)

#Average marks by city
if "City" in df.columns and "Marks" in df.columns:
    print("\n--- Average Marks by City ---")
    city_marks = df.groupby("City")["Marks"].mean()
    print(city_marks)

#detect outliers using IQR
print("\n--- Outlier Detection ---")
for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]
    print(f"\nColumn: {column}")
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Outliers:", len(outliers))
    if len(outliers) > 0:
        print(outliers)

#Key Business Questions 
print("\n--- KEY BUSINESS QUESTIONS ---")

# Question 1: Average marks
if "Marks" in df.columns:

    average_marks = df["Marks"].mean()

    print("\n1. What is the average student performance?")
    print("Average Marks:", round(average_marks, 2))


# Question 2: Highest performing course
if "Course" in df.columns and "Marks" in df.columns:

    course_average = df.groupby("Course")["Marks"].mean()

    print("\n2. What is the average performance by course?")
    print(course_average)

    highest_course = course_average.idxmax()

    print(
        "Course with highest average marks:",
        highest_course
    )


# Question 3: Highest performing city
if "City" in df.columns and "Marks" in df.columns:

    city_average = df.groupby("City")["Marks"].mean()

    print("\n3. What is the average performance by city?")
    print(city_average)

    highest_city = city_average.idxmax()

    print(
        "City with highest average marks:",
        highest_city
    )


# Question 4: Highest individual score
if "Marks" in df.columns:

    highest_marks = df["Marks"].max()

    print("\n4. What is the highest score?")
    print("Highest Marks:", highest_marks)

    top_student = df.loc[df["Marks"].idxmax(), "Name"]

    print("Student with highest marks:", top_student)


# Question 5: Lowest individual score
if "Marks" in df.columns:

    lowest_marks = df["Marks"].min()

    print("\n5. What is the lowest score?")
    print("Lowest Marks:", lowest_marks)        

#Generate Short Report
print("\n" + "=" * 60)
print("SHORT ANALYSIS REPORT")
print("=" * 60)

print(f"""
The dataset contains {df.shape[0]} records and {df.shape[1]} features.

The average marks are {df["Marks"].mean():.2f}.
The highest marks are {df["Marks"].max()}.
The lowest marks are {df["Marks"].min()}.

The standard deviation of marks is
{df["Marks"].std():.2f}, which indicates the spread
of student performance.

The course with the highest average performance is
{df.groupby("Course")["Marks"].mean().idxmax()}.

The city with the highest average performance is
{df.groupby("City")["Marks"].mean().idxmax()}.

Correlation analysis can be used to understand
relationships between numerical variables.

The IQR method was used to identify potential
outliers and unusual observations.
""")

print("\nAnalysis completed successfully.")
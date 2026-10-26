import pandas as pd
import matplotlib.pyplot as plt

# 1. Read CSV file into a DataFrame
df = pd.read_csv("student.csv")

# 2. Display first five records and dataset information
print("----- First Five Student Records -----")
print(df.head())

print("\n----- Dataset Information -----")
print(df.info())

# 3. Calculate average, maximum, and minimum marks
print("\n----- Marks Analysis -----")
print("Average Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

# 4. Identify students scoring more than 75 marks
print("\n----- Students Scoring More Than 75 Marks -----")
high_scorers = df[df["Marks"] > 75]
print(high_scorers)

# 5. Bar chart showing marks obtained by each student
plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Marks"], color="skyblue")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Histogram showing distribution of student marks
plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5, color="orange", edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")
plt.tight_layout()
plt.show()

# 7. Scatter plot showing relationship between study hours and marks
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Marks"], color="green")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.grid(True)
plt.tight_layout()
plt.show()
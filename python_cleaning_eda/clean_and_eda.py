import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Load dataset
df = pd.read_csv(r"D:\dataset\student_habits_performance\student_habits_performance.csv")
print(df)
df.info()

# Data cleaning and check missing values
df["parental_education_level"].fillna("Unknown",inplace=True)
print(df.isnull().sum())
df["exam_score"] = df["exam_score"].round()

bins = [0, 50, 80, 100]
labels = ["Low Score", "Mid Scores", "High Scores"]
df["Score_Category"] = pd.cut(df["exam_score"], bins = bins, labels = labels, include_lowest = True)
print(df.head())

# Visualization (Study hours impact to exam scores)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="exam_score", y="study_hours_per_day", color="Olivedrab")
plt.title("The Impact Study Hours on Exam Scores")
plt.xlabel("exam score")
plt.ylabel("study hours per day")
plt.tight_layout()
plt.savefig("plot_scatter_exam_vs_studyhours.png")
plt.show()


df.to_csv(r"D:\dataset\student_habits_performance\student_habits_performance_EDA.csv", index=False)

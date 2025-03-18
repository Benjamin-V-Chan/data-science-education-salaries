import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_salaries.csv")

# Compute basic statistics
summary = df.describe()

# Identify highest and lowest-paying majors
highest_paying = df.nlargest(5, "Mid-Career Pay")
lowest_paying = df.nsmallest(5, "Mid-Career Pay")

# Save results
summary.to_csv("outputs/summary_statistics.csv")
highest_paying.to_csv("outputs/highest_paying_majors.csv", index=False)
lowest_paying.to_csv("outputs/lowest_paying_majors.csv", index=False)

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/cleaned_salaries.csv")

# Histogram of Early Career Pay
plt.hist(df["Early Career Pay"], bins=20, edgecolor="black")
plt.xlabel("Early Career Pay")
plt.ylabel("Frequency")
plt.title("Distribution of Early Career Pay")
plt.savefig("outputs/early_career_pay_histogram.png")
plt.close()

# Scatter plot: Early Career Pay vs. Mid-Career Pay
plt.scatter(df["Early Career Pay"], df["Mid-Career Pay"], alpha=0.5)
plt.xlabel("Early Career Pay")
plt.ylabel("Mid-Career Pay")
plt.title("Early Career Pay vs. Mid-Career Pay")
plt.savefig("outputs/scatter_salary_growth.png")
plt.close()

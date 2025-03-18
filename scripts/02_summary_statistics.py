import pandas as pd

# Load dataset
df = pd.read_csv("data/final-post-college-salaries.csv")

# Convert salary columns to numeric values
df["Early Career Pay"] = df["Early Career Pay"].replace("[$,]", "", regex=True).astype(float)
df["Mid-Career Pay"] = df["Mid-Career Pay"].replace("[$,]", "", regex=True).astype(float)
df["% High Meaning"] = df["% High Meaning"].replace("[%]", "", regex=True).astype(float)

# Save cleaned data
df.to_csv("data/cleaned_salaries.csv", index=False)

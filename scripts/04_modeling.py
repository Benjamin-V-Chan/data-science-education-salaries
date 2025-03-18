import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load cleaned dataset
df = pd.read_csv("data/cleaned_salaries.csv")

# Features and target variable
X = df[["Early Career Pay"]]
y = df["Mid-Career Pay"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save results
with open("outputs/model_performance.txt", "w") as f:
    f.write(f"Mean Absolute Error: {mae:.2f}\n")
    f.write(f"R-squared: {r2:.2f}\n")

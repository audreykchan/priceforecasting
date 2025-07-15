# Visualizing revenue as plots + graphs

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

conn = sqlite3.connect("pos_data.db")
query = """
    SELECT
        DATE(timestamp) AS day,
        SUM(total_amount) AS total_revenue
    FROM
        transactions
    GROUP BY
        day
    ORDER BY
        day ASC;
"""

# Load results in df
df = pd.read_sql_query(query, conn)

# Convert day column to date time
df["day"] = pd.to_datetime(df["day"])

# Plot
plt.figure(figsize=(12, 5))
plt.plot(df["day"], df["total_revenue"], marker='o', linewidth=2)
plt.title("Daily Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Total Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Day to integer index for the x axis
df["day_index"] = (df["day"] - df["day"].min()).dt.days

# Reshape into model input
X = df["day_index"].values.reshape(-1, 1)
y = df["total_revenue"].values

model = LinearRegression()
model.fit(X,y)

# Future forecasting for next 7 days
future_days = np.arange(df["day_index"].max() + 1, df["day_index"].max()+8).reshape(-1,1)
future_revenue = model.predict(future_days)

# Print predictions within range of 7 days
print("\nPredicted revenue for next 7 days:")
for i in range(7):
    future_date = df["day"].max() + pd.Timedelta(days=i+1)
    print(f"{future_date.date()}: ${future_revenue[i]:.2f}")

# Combined df of actual and predicted
future_dates = [df["day"].max() + pd.Timedelta(days=i+1) for i in range(7)]

forecast_df = pd.DataFrame({
    "day": future_dates,
    "total_revenue": future_revenue
})

full_df = pd.concat([df[["day", "total_revenue"]], forecast_df], ignore_index=True)

# Plot
plt.figure(figsize=(12, 5))
plt.plot(df["day"], df["total_revenue"], label="Actual", marker="o")
plt.plot(forecast_df["day"], forecast_df["total_revenue"], label="Forecast", marker="x", linestyle="--", color="orange")
plt.title("Revenue Forecast (Linear Regression)")
plt.xlabel("Date")
plt.ylabel("Total Revenue ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
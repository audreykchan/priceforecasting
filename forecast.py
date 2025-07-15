'''
from sklearn.linear_model import LinearRegression
import numpy as np
import sqlite3

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
    '''
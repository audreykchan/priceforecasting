import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import io
import base64

st.title("Price Model & Revenue Forecasting Dashboard")

# Slider for price range
price = st.slider("Set Price ($)", min_value=2.0, max_value=10.0, step=0.1, value=5.0)

# Demand curve
max_quantity = 120
slope = 10
quantity = max(max_quantity - slope * price, 0)
revenue = price * quantity

st.write(f"**Predicted Quantity Sold:** {quantity:.2f}")
st.write(f"**Predicted Revenue:** ${revenue:.2f}")

# Full demand & rev curves
prices = np.linspace(2, 10, 50)
quantities = np.maximum(max_quantity - slope * prices, 0)
revenues = prices * quantities

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(prices, quantities, label="Demand", color="green")
ax1.axvline(price, color="gray", linestyle="--")
ax1.set_title("Demand Curve")
ax1.set_xlabel("Price ($)")
ax1.set_ylabel("Quantity Sold")
ax1.grid(True)

ax2.plot(prices, revenues, label="Revenue", color="blue")
ax2.axvline(price, color="gray", linestyle="--")
ax2.set_title("Revenue Curve")
ax2.set_xlabel("Price ($)")
ax2.set_ylabel("Revenue ($)")
ax2.grid(True)

st.pyplot(fig)

# Load data
df = pd.read_csv("pos_transactions.csv")

# Category filter
if "product_category" in df.columns:
    selected_category = st.selectbox("Select Product Category", df["product_category"].unique())
    filtered_df = df[df["product_category"] == selected_category]
else:
    st.error("Missing 'product_category' column.")
    st.stop()

st.header("Real Demand Curve from Transaction Data")

# Price bins
# GOOD — use the filtered data
filtered_df["price_bin"] = pd.cut(filtered_df["unit_price"], bins=np.arange(2, 10.5, 0.5))

elasticity_df = filtered_df.groupby("price_bin", observed=False).agg({
    "unit_price": "mean",
    "quantity": "mean",
    "transaction_id": "count"
}).reset_index()


# Drop NaNs if any
elasticity_df.dropna(inplace=True)

# Plot quantity vs price
fig = plt.figure(figsize=(6, 4))
plt.plot(elasticity_df["unit_price"], elasticity_df["quantity"], marker='o')
plt.title("Quantity Sold vs. Price (Historical Data)")
plt.xlabel("Unit Price ($)")
plt.ylabel("Average Quantity Sold")
plt.grid(True)
st.pyplot(fig)

st.subheader("Fitted Demand Model + Elasticity")

# Data for model
X = elasticity_df["unit_price"].values.reshape(-1, 1)
y = elasticity_df["quantity"].values

model = LinearRegression()
model.fit(X, y)

fitted_quantities = model.predict(X)

# Actual vs predicted fitted plot
fig2 = plt.figure(figsize=(6, 4))
plt.scatter(X, y, label="Actual", color="blue")
plt.plot(X, fitted_quantities, label="Fitted Line", color="red")
plt.title("Fitted Linear Demand Curve")
plt.xlabel("Unit Price ($)")
plt.ylabel("Avg Quantity Sold")
plt.legend()
plt.grid(True)
st.pyplot(fig2)

slope = model.coef_[0]
intercept = model.intercept_
st.write(f"**Fitted Model:** Quantity = {intercept:.2f} + ({slope:.2f} × Price)")

# Downloadable CSV (filtered data)
csv = filtered_df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
st.markdown(f" [Download Filtered Data as CSV](data:file/csv;base64,{b64})", unsafe_allow_html=True)

# Save figure to buffer (most recent figure plotted)
buf = io.BytesIO()
fig2.savefig(buf, format="png")
buf.seek(0)
b64_img = base64.b64encode(buf.read()).decode()
st.markdown(
    f'<a href="data:image/png;base64,{b64_img}" download="fitted_demand_curve.png"> Download Fitted Demand Curve</a>',
    unsafe_allow_html=True
)
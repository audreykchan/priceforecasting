import numpy as np
import matplotlib.pyplot as plt

prices = np.linspace(2, 10, 50)


# Demand decreases as price increases (linear relationship)
quantities = 120 - 10 * prices
quantities = np.maximum(quantities, 0) #negative values to 0
revenue = prices * quantities

plt.figure(figsize=(12, 5))

# Demand curve
plt.subplot(1, 2, 1)
plt.plot(prices, quantities, label="Demand", color="green")
plt.title("Simulated Demand Curve")
plt.xlabel("Price ($)")
plt.ylabel("Quantity Sold")
plt.grid(True)

# Revenue curve
plt.subplot(1, 2, 2)
plt.plot(prices, revenue, label="Revenue", color="blue")
plt.title("Simulated Revenue Curve")
plt.xlabel("Price ($)")
plt.ylabel("Revenue ($)")
plt.grid(True)

plt.tight_layout()
plt.show()
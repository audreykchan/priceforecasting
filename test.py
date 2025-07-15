import pandas as pd

df = pd.read_csv("pos_transactions.csv")

# Show all transactions w/ qty > 3
filtered = df[df["quantity"] > 3]

print(filtered.head())
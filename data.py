import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

num_rows=1000
store_ids=[f"store_{i}" for i in range(1,11)]
categories=["basic_item", "premium_item", "subscription", "one_time_service", "enterprise"] #fake cats

def random_date():
    start = datetime.now() - timedelta(days=90)
    end = datetime.now()
    return start + (end - start) * random.random()

data = {
    "transaction_id": [f"txn_{i}" for i in range(num_rows)],
    "store_id": np.random.choice(store_ids, size=num_rows),
    "timestamp": [random_date() for _ in range(num_rows)],
    "product_category": np.random.choice(categories, size=num_rows),
    "quantity": np.random.randint(1, 6, size=num_rows),
    "unit_price": np.random.uniform(2.0, 8.0, size=num_rows).round(2),
}

df = pd.DataFrame(data)
df["total_amount"] = (df["quantity"] * df["unit_price"]).round(2)

# Save to CSV
df.to_csv("pos_transactions.csv", index=False)

# First 5 rows
print(df.head())
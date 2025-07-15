# Total revenue by category

import sqlite3
conn = sqlite3.connect("pos_data.db")
cursor = conn.cursor()

query = """

SELECT
    product_category,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM
    transactions
GROUP BY
    product_category
ORDER BY
    total_revenue DESC;

"""
# Gets results from executed query
cursor.execute(query)
rows = cursor.fetchall()

# Print rows
for row in rows:
    print(row)

conn.close()
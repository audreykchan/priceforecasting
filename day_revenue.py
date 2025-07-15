# Finding the revenue categorized by date (chronologically)

import sqlite3

conn = sqlite3.connect("pos_data.db")
cursor = conn.cursor()

query = """

SELECT
    DATE(timestamp) AS day,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM
    transactions
GROUP BY
    day
ORDER BY
    day ASC
"""

cursor.execute(query)
rows = cursor.fetchall()

print("Revenue by day:\n")
for row in rows:
    print(rows)

conn.close()

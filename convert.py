# Code to load csv into SQLite
import pandas as pd
import sqlite3

# Load csv
df = pd.read_csv("pos_transactions.csv")

# Connect sqlite to pos_data.db
conn = sqlite3.connect("pos_data.db")

# Write the DataFrame to a new SQL table
df.to_sql("transactions", conn, if_exists="replace", index=False)

# 1st 5 rows
cursor = conn.cursor()
cursor.execute("SELECT * FROM transactions LIMIT 5;")
rows = cursor.fetchall()

#Print rows
for row in rows:
    print(row)

conn.close()

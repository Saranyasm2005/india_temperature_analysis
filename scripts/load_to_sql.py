import pandas as pd
import sqlite3

# Load cleaned CSV
df = pd.read_csv("clean_temperature_data.csv")

# Connect to SQLite database
conn = sqlite3.connect("india_temperature.db")

# Load data into SQL table
df.to_sql("india_temperature", conn, if_exists="replace", index=False)

conn.close()

print("✅ Data successfully loaded into SQL database")

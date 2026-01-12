import sqlite3
import pandas as pd

# -----------------------------------
# Connect to SQLite Database
# -----------------------------------
conn = sqlite3.connect("india_temperature.db")

# -----------------------------------
# 1. Check total number of records
# -----------------------------------
query_count = """
SELECT COUNT(*) AS total_records
FROM india_temperature;
"""
df_count = pd.read_sql(query_count, conn)
print("\n🔹 Total Records:")
print(df_count)

# -----------------------------------
# 2. Average Annual Temperature
# -----------------------------------
query_avg_annual = """
SELECT AVG(ANNUAL) AS avg_annual_temperature
FROM india_temperature;
"""
df_avg_annual = pd.read_sql(query_avg_annual, conn)
print("\n🔹 Average Annual Temperature:")
print(df_avg_annual)

# -----------------------------------
# 3. Decadal Average Temperature Trend
# -----------------------------------
query_decadal = """
SELECT (YEAR/10)*10 AS decade,
       AVG(ANNUAL) AS avg_annual_temperature
FROM india_temperature
GROUP BY decade
ORDER BY decade;
"""
df_decadal = pd.read_sql(query_decadal, conn)
print("\n🔹 Decadal Average Temperature Trend:")
print(df_decadal)

# -----------------------------------
# 4. Seasonal Average Temperatures
# -----------------------------------
query_seasonal = """
SELECT
    AVG(JAN_FEB) AS avg_jan_feb,
    AVG(MAR_MAY) AS avg_mar_may,
    AVG(JUN_SEP) AS avg_jun_sep,
    AVG(OCT_DEC) AS avg_oct_dec
FROM india_temperature;
"""
df_seasonal = pd.read_sql(query_seasonal, conn)
print("\n🔹 Average Seasonal Temperatures:")
print(df_seasonal)

# -----------------------------------
# 5. Recent Years Temperature (Post-1980)
# -----------------------------------
query_recent = """
SELECT YEAR, ANNUAL
FROM india_temperature
WHERE YEAR >= 1980
ORDER BY YEAR;
"""
df_recent = pd.read_sql(query_recent, conn)
print("\n🔹 Recent Years Temperature (Post-1980):")
print(df_recent.head())

# -----------------------------------
# Close database connection
# -----------------------------------
conn.close()

print("\n✅ SQL analysis completed successfully")


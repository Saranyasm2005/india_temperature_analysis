
import pandas as pd

# Load CSV file (correct function + correct path)
df = pd.read_csv("data/indiantemp.csv")

print(df.head())
print(df.info())

# Rename columns (adjust if your CSV header differs)
df.columns = ['YEAR','ANNUAL','JAN_FEB','MAR_MAY','JUN_SEP','OCT_DEC']

# Convert temperature columns to numeric
cols = ['ANNUAL','JAN_FEB','MAR_MAY','JUN_SEP','OCT_DEC']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# Save cleaned CSV
df.to_csv("clean_temperature_data.csv", index=False)

print("✅ CSV data cleaned successfully")


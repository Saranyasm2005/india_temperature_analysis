
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =============================
# Load cleaned data
# =============================
df = pd.read_csv("clean_temperature_data.csv")

# =============================
# Data Cleaning (SAFE)
# =============================

# Clean YEAR column
df['YEAR'] = pd.to_numeric(df['YEAR'], errors='coerce')
df = df.dropna(subset=['YEAR'])
df['YEAR'] = df['YEAR'].astype(int)

# Clean temperature columns
temp_cols = ['ANNUAL','JAN_FEB','MAR_MAY','JUN_SEP','OCT_DEC']
df[temp_cols] = df[temp_cols].apply(pd.to_numeric, errors='coerce')
df = df.dropna(subset=['ANNUAL'])

print(df.head())
print(df.info())

# =============================
# 1. Annual Temperature Trend
# =============================
plt.figure(figsize=(10,5))
plt.plot(df['YEAR'], df['ANNUAL'], color='red')
plt.title("Annual Mean Temperature Trend in India (1901–2021)")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# =============================
# 2. Seasonal Average Comparison
# =============================
seasonal_avg = df[['JAN_FEB','MAR_MAY','JUN_SEP','OCT_DEC']].mean()

plt.figure(figsize=(7,5))
seasonal_avg.plot(kind='bar')
plt.title("Average Seasonal Temperatures in India")
plt.ylabel("Temperature (°C)")
plt.grid(axis='y')
plt.show()

# =============================
# 3. Decadal Analysis
# =============================
df['DECADE'] = (df['YEAR'] // 10) * 10
decadal_avg = df.groupby('DECADE')['ANNUAL'].mean()

plt.figure(figsize=(10,5))
plt.plot(decadal_avg.index, decadal_avg.values, marker='o')
plt.title("Decadal Average Temperature Trend")
plt.xlabel("Decade")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# =============================
# 4. Rolling Average Analysis
# =============================
df['ROLLING_5'] = df['ANNUAL'].rolling(5).mean()
df['ROLLING_10'] = df['ANNUAL'].rolling(10).mean()

plt.figure(figsize=(10,5))
plt.plot(df['YEAR'], df['ANNUAL'], color='lightgray', label='Annual')
plt.plot(df['YEAR'], df['ROLLING_5'], color='blue', label='5-Year Avg')
plt.plot(df['YEAR'], df['ROLLING_10'], color='red', label='10-Year Avg')
plt.title("Annual Temperature with Rolling Averages")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()

# =============================
# 5. Temperature Anomaly Analysis
# =============================
baseline = df[(df['YEAR'] >= 1901) & (df['YEAR'] <= 1950)]['ANNUAL'].mean()
df['ANOMALY'] = df['ANNUAL'] - baseline

plt.figure(figsize=(10,5))
plt.bar(df['YEAR'], df['ANOMALY'], color='orange')
plt.axhline(0, color='black')
plt.title("Temperature Anomalies (Baseline: 1901–1950)")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.grid(True)
plt.show()

# =============================
# 6. Linear Trend Analysis (SAFE)
# =============================
df_lr = df[['YEAR','ANNUAL']].dropna()

x = df_lr['YEAR'].values
y = df_lr['ANNUAL'].values

z = np.polyfit(x, y, 1)
trend = np.poly1d(z)

plt.figure(figsize=(10,5))
plt.plot(x, y, color='lightgray', label='Annual')
plt.plot(x, trend(x), color='red', label='Trend Line')
plt.title("Linear Trend of Annual Mean Temperature")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()

print(f"🔥 Warming rate: {z[0]:.4f} °C per year")
print("✅ Advanced analysis completed successfully")

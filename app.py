
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="India Temperature Analysis",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ India Temperature Analysis (1901–2021)")
st.markdown(
    """
    **Dataset Source:** data.gov.in  
    **Objective:** Analyze long-term temperature trends in India using seasonal,
    annual, and decadal patterns.
    """
)

# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("clean_temperature_data.csv")

df = load_data()

# -----------------------------
# Sidebar controls
# -----------------------------
st.sidebar.header("🔎 Filters")

year_min = int(df["YEAR"].min())
year_max = int(df["YEAR"].max())

year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=year_min,
    max_value=year_max,
    value=(year_min, year_max)
)

filtered_df = df[
    (df["YEAR"] >= year_range[0]) &
    (df["YEAR"] <= year_range[1])
].copy()

# -----------------------------
# Data preview
# -----------------------------
with st.expander("📄 View Dataset"):
    st.dataframe(filtered_df)

# =============================
# SECTION 1: Annual Trend
# =============================
st.subheader("📈 Annual Mean Temperature Trend")

fig1, ax1 = plt.subplots()
ax1.plot(filtered_df["YEAR"], filtered_df["ANNUAL"], color="red")
ax1.set_xlabel("Year")
ax1.set_ylabel("Temperature (°C)")
ax1.set_title("Annual Mean Temperature Trend")
ax1.grid(True)

st.pyplot(fig1)

# =============================
# SECTION 2: Seasonal Averages
# =============================
st.subheader("🌦️ Average Seasonal Temperatures")

seasonal_avg = filtered_df[
    ["JAN_FEB", "MAR_MAY", "JUN_SEP", "OCT_DEC"]
].mean()

fig2, ax2 = plt.subplots()
seasonal_avg.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Temperature (°C)")
ax2.set_title("Average Seasonal Temperatures")
ax2.grid(axis="y")

st.pyplot(fig2)

# =============================
# SECTION 3: Decadal Trend
# =============================
st.subheader("📊 Decadal Average Temperature Trend")

filtered_df["DECADE"] = (filtered_df["YEAR"] // 10) * 10
decadal_avg = filtered_df.groupby("DECADE")["ANNUAL"].mean()

fig3, ax3 = plt.subplots()
ax3.plot(decadal_avg.index, decadal_avg.values, marker="o")
ax3.set_xlabel("Decade")
ax3.set_ylabel("Temperature (°C)")
ax3.set_title("Decadal Average Temperature")
ax3.grid(True)

st.pyplot(fig3)

# =============================
# SECTION 4: Rolling Average
# =============================
st.subheader("📉 Rolling Average Analysis")

filtered_df["ROLL_5"] = filtered_df["ANNUAL"].rolling(5).mean()
filtered_df["ROLL_10"] = filtered_df["ANNUAL"].rolling(10).mean()

fig4, ax4 = plt.subplots()
ax4.plot(filtered_df["YEAR"], filtered_df["ANNUAL"], color="lightgray", label="Annual")
ax4.plot(filtered_df["YEAR"], filtered_df["ROLL_5"], label="5-Year Avg")
ax4.plot(filtered_df["YEAR"], filtered_df["ROLL_10"], label="10-Year Avg")

ax4.set_xlabel("Year")
ax4.set_ylabel("Temperature (°C)")
ax4.set_title("Rolling Average Temperature Trends")
ax4.legend()
ax4.grid(True)

st.pyplot(fig4)

# =============================
# SECTION 5: Temperature Anomaly
# =============================
st.subheader("🌡️ Temperature Anomaly (Baseline 1901–1950)")

baseline = df[(df["YEAR"] >= 1901) & (df["YEAR"] <= 1950)]["ANNUAL"].mean()
filtered_df["ANOMALY"] = filtered_df["ANNUAL"] - baseline

fig5, ax5 = plt.subplots()
ax5.bar(filtered_df["YEAR"], filtered_df["ANOMALY"], color="orange")
ax5.axhline(0, color="black")
ax5.set_xlabel("Year")
ax5.set_ylabel("Anomaly (°C)")
ax5.set_title("Temperature Anomalies")
ax5.grid(True)

st.pyplot(fig5)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "👨‍🎓 **Final Year Data Analytics Project**  \n"
    "Tools: Python • Pandas • Matplotlib • Streamlit • SQL (optional)"
)

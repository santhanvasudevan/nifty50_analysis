import streamlit as st
import pandas as pd
import glob
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit Page Config
st.set_page_config(page_title="Stock Market Dashboard", layout="wide")

st.title("📊 Stock Market Analysis Dashboard")

# Load CSV Files
csv_files = glob.glob(r"AI ML\Stock Market Analysis\output\individual_output_csv\*.csv")  # Adjust path
sector_df = pd.read_csv(r"AI ML\Stock Market Analysis\input\sector_data.csv")  # Load sector mapping

all_data = []  # List to store all stock data
unique_data = {}  # Dictionary to store unique stock data

for file in csv_files:
    df = pd.read_csv(file)

    ticker = df.iloc[0]["Ticker"]  # Get the ticker
    
    if ticker not in unique_data:
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")
        df["daily_return"] = df["close"].pct_change()  # Calculate daily return
        df["Ticker"] = ticker  # Ensure Ticker is set properly

        unique_data[ticker] = df  # Store unique stock data

# Combine unique stock data into one DataFrame
stock_df = pd.concat(unique_data.values(), ignore_index=True)


# Rename columns to match expected names
sector_df.rename(columns={"Symbol": "Ticker", "sector": "Sector"}, inplace=True)

sector_df["Ticker"] = sector_df["Ticker"].str.split(": ").str[-1]

# Ensure Sector Mapping is Merged
stock_df = stock_df.merge(sector_df, on="Ticker", how="left")

### 1️⃣ Volatility Analysis - Standard Deviation of Daily Returns ###
st.subheader("📌 Volatility Analysis - Most Volatile Stocks")

volatility_df = stock_df.groupby("Ticker")["daily_return"].std().reset_index()
volatility_df.columns = ["Ticker", "Volatility"]
top_10_volatile = volatility_df.nlargest(10, "Volatility")

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x="Ticker", y="Volatility", data=top_10_volatile, ax=ax, palette="Reds")
ax.set_title("Top 10 Most Volatile Stocks")
ax.set_ylabel("Standard Deviation of Daily Returns")
ax.set_xlabel("Stock Ticker")
st.pyplot(fig)


### 2️⃣ Cumulative Return Over Time ###
st.subheader("📈 Cumulative Return of Top Performing Stocks")

stock_df["cumulative_return"] = stock_df.groupby("Ticker")["daily_return"].cumsum()

top_5_performing = volatility_df.nlargest(5, "Volatility")["Ticker"].tolist()
filtered_df = stock_df[stock_df["Ticker"].isin(top_5_performing)]

fig, ax = plt.subplots(figsize=(12, 6))
for ticker in top_5_performing:
    subset = filtered_df[filtered_df["Ticker"] == ticker]
    ax.plot(subset["date"], subset["cumulative_return"], label=ticker)

ax.set_title("Cumulative Return of Top 5 Performing Stocks")
ax.set_xlabel("Date")
ax.set_ylabel("Cumulative Return")
ax.legend()
st.pyplot(fig)

### 3️⃣ Sector-Wise Performance ###
st.subheader("📌 Sector-wise Performance")

sector_performance = stock_df.groupby("Sector")["daily_return"].mean().reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x="Sector", y="daily_return", data=sector_performance, ax=ax, palette="coolwarm")
ax.set_title("Average Yearly Return by Sector")
ax.set_ylabel("Average Return (%)")
ax.set_xlabel("Sector")
plt.xticks(rotation=90)
st.pyplot(fig)

### 4️⃣ Stock Price Correlation Heatmap ###
st.subheader("📊 Stock Price Correlation Heatmap")

stock_df = stock_df.drop_duplicates(subset=["date", "Ticker"])
pivot_df = stock_df.pivot(index="date", columns="Ticker", values="close").dropna()
corr_matrix = pivot_df.corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, cmap="coolwarm", annot=False, linewidths=0.5, ax=ax)
ax.set_title("Stock Price Correlation Heatmap")
st.pyplot(fig)

### 5️⃣ Top 5 Gainers and Losers (Month-wise) ###
st.subheader("📅 Monthly Top Gainers & Losers")

stock_df["month"] = stock_df["date"].dt.strftime("%Y-%m")
monthly_returns = stock_df.groupby(["month", "Ticker"])["daily_return"]\
    .apply(lambda x: (x.add(1).prod() - 1) * 100)\
    .reset_index().rename(columns={"daily_return": "Monthly_return"})  # Rename column

monthly_returns["Monthly_return"] = monthly_returns["Monthly_return"].apply(lambda x: round(x, 1))

for month in stock_df["month"].unique():
    st.subheader(f"📆 {month}")
    
    monthly_data = monthly_returns[monthly_returns["month"] == month]
    top_5_gainers = monthly_data.nlargest(5, "Monthly_return")
    top_5_losers = monthly_data.nsmallest(5, "Monthly_return")

    col1, col2 = st.columns(2)

    with col1:
        st.write("🐂📈 **Top 5 Gainers**")
        st.dataframe(top_5_gainers)

    with col2:
        st.write("🐻📉 **Top 5 Losers**")
        st.dataframe(top_5_losers)

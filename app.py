import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st

# Load data
df = pd.read_csv("Nifty_Stocks.csv")
df.Date = pd.to_datetime(df.Date)

st.title("Nifty Stock Price Viewer 📈")

# Sidebar for user inputs
category = st.sidebar.selectbox("Select Category", df['Category'].unique())

# Filter based on selected category
filtered_df = df[df['Category'] == category]
symbols = filtered_df['Symbol'].unique()

symbol = st.sidebar.selectbox("Select Symbol", symbols)

# Filter based on selected symbol
final_df = filtered_df[filtered_df['Symbol'] == symbol]

# Plotting
st.subheader(f"Closing Price of {symbol} over Time")

fig, ax = plt.subplots(figsize=(10, 4))
sb.lineplot(data=final_df, x='Date', y='Close', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

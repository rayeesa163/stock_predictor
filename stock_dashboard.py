# app.py
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trader Pro Dashboard", layout="wide")

st.title("📈 Professional Trading Dashboard")
st.subheader("Inspired by Warren Buffett’s long-term investing style")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT, TSLA)", "AAPL")

if ticker:
    data = yf.download(ticker, period="6mo")
    st.write(f"### Last 6 months data for {ticker}")
    st.dataframe(data.tail())

    # Plot
    fig, ax = plt.subplots(figsize=(10, 4))
    data["Close"].plot(ax=ax, title=f"{ticker} Closing Prices")
    st.pyplot(fig)

    # Show basic stats
    st.write("### Key Stats")
    st.write(data.describe())

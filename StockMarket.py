
import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Market Data")

ticker_symbol = st.text_input("Enter the stock ticker", "AAPL")

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start Date", value=datetime.date(2019, 1, 7))
with col2:
    end_date = st.date_input("End Date", value=datetime.date(2023, 1, 7))

data = yf.download(ticker_symbol, start=start_date, end=end_date)

st.write(data)

st.line_chart(data["Close"])

st.bar_chart(data["Volume"])
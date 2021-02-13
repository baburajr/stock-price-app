import pandas as pd
import streamlit as st
import yfinance as yf


st.write("""
# Simple Stock Price App

Shown are the closing prices of different stocks on my watchlist

""")

tikrSymbol = 'GOOGL'

tikrData = yf.Ticker(tikrSymbol)

tikrDf = tikrData.history(period='1d', start='2010-1-31', end='2021-2-12')

st.write("""
### Closing Price
""")
st.line_chart(tikrDf.Close)
st.line_chart(tikrDf.Volume)
import yfinance as yf
import pandas as pd

def fetch_historical_data(symbol, period='1mo'):
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)
    return data

symbol = 'SBIN.NS'  
period = '1mo'      

historical_data = fetch_historical_data(symbol, period)
if not historical_data.empty:
    print(historical_data)
else:
    print(f"No data found for symbol {symbol} in the period {period}")

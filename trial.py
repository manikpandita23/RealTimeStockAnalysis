import yfinance as yf
import pandas as pd

def fetch_historical_data(symbol, period='1mo'):
    # Fetch historical data using yfinance
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)
    return data

# Example usage
symbol = 'SBIN.NS'  # NSE symbols need to end with '.NS'
period = '1mo'      # You can specify '1mo', '3mo', '6mo', '1y', etc.

historical_data = fetch_historical_data(symbol, period)
if not historical_data.empty:
    print(historical_data)
else:
    print(f"No data found for symbol {symbol} in the period {period}")

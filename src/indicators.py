import pandas as pd

def moving_average(data):
    data["20_day_avg"] = data["Close"].rolling(window=20).mean()
    data["50_day_avg"] = data["Close"].rolling(window=50).mean()

def relative_strength_index(data, period=14):
    theta = data["Close"].diff()
    gain = theta.where(theta > 0, 0).rolling(window=period).mean()
    loss = -theta.where(theta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    data["RSI"] = 100 - (100 / (1 + rs))

def average_volume(data, period=20):
    data["avg_volume"] = data["Volume"].rolling(window=period).mean()

def volatility(data, period=20):
    data["volatility"] = data["Close"].rolling(window=period).std()

def MACD(data,short_period=12, long_period=26, signal_period=9):
    data["EMA_Short"] = data["Close"].ewm(span=short_period, adjust=False).mean()
    data["EMA_Long"] = data["Close"].ewm(span=long_period, adjust=False).mean()
    data["MACD"] = data["EMA_Short"] - data["EMA_Long"]
    data["Signal_Line"] = data["MACD"].ewm(span=signal_period, adjust=False).mean()
    data["MACD_Histogram"] = data["MACD"] - data["Signal_Line"]
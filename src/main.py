from data import get_stock_data
from indicators import *




data = get_stock_data('AAPL')
moving_average(data)
relative_strength_index(data)
MACD(data)
average_volume(data)
volatility(data)

print(data[["Close", "20_day_avg", "50_day_avg", "RSI","Signal_Line","MACD_Histogram","avg_volume","volatility","EMA_Short","EMA_Long"]].tail(10))
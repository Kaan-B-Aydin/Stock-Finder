from data import get_stock_data
from indicators import *




data = get_stock_data('AAPL')
moving_average(data)


print(data[["Close", "20_day_avg"]].tail(10))
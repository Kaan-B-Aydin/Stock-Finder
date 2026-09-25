import pandas as pd

def moving_average(data):
    data["20_day_avg"] = data["Close"].rolling(window=20).mean()

    
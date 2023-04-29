from binance.client import Client
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns

# LEAVE THE API UNTOUCHED IF YOU DON'T NEED THEM
api_key = 'your_api_key'
api_secret = 'your_api_secret'

client = Client(api_key, api_secret)

# CHOOSE THE LISTED PAIR ON BINANCE
symbol = 'BTCUSDT'

# DEFINE INTERVALS
interval_1MINUTE = Client.KLINE_INTERVAL_1MINUTE
interval_15MINUTE = Client.KLINE_INTERVAL_15MINUTE
interval_5MINUTE = Client.KLINE_INTERVAL_5MINUTE
interval_1HOUR = Client.KLINE_INTERVAL_1HOUR
interval_4HOUR = Client.KLINE_INTERVAL_4HOUR
interval_1DAY = Client.KLINE_INTERVAL_1DAY
interval_1WEEK = Client.KLINE_INTERVAL_1WEEK

# DEFINE START DATE OF EVERY TIMEFRAME
start_date_1MINUTE = '25 Apr, 2023'
start_date_5MINUTE = '20 Apr, 2023'
start_date_15MINUTE = '26 Mar, 2023'
start_date_1HOUR = '1 Jan, 2023'
start_date_4HOUR = '1 Jan, 2022'
start_date_1DAY = '13 Feb, 2020'
start_date_1WEEK = '13 Feb, 2020'

# END DATE = SET TODAY DATE
end_date = '30 Apr, 2023'

# DEFINE OBJECT CANDLES (LISTS)
candle_1MINUTE = client.get_historical_klines(symbol, interval_1MINUTE, start_date_1MINUTE, end_date)
candle_5MINUTE = client.get_historical_klines(symbol, interval_5MINUTE, start_date_5MINUTE, end_date)
candle_15MINUTE = client.get_historical_klines(symbol, interval_15MINUTE, start_date_15MINUTE, end_date)
candle_1HOUR = client.get_historical_klines(symbol, interval_1HOUR, start_date_1HOUR, end_date)
candle_4HOUR = client.get_historical_klines(symbol, interval_4HOUR, start_date_4HOUR, end_date)
candle_1DAY = client.get_historical_klines(symbol, interval_1DAY, start_date_1DAY, end_date)
candle_1WEEK = client.get_historical_klines(symbol, interval_1WEEK, start_date_1WEEK, end_date)

# CREATE DATAFRAME OBJECTS
candle_1MINUTE = pd.DataFrame(candle_1MINUTE, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
candle_1MINUTE['timestamp'] = pd.to_datetime(candle_1MINUTE['timestamp'], unit='ms')

candle_5MINUTE = pd.DataFrame(candle_5MINUTE, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
candle_5MINUTE['timestamp'] = pd.to_datetime(candle_5MINUTE['timestamp'], unit='ms')

candle_15MINUTE = pd.DataFrame(candle_5MINUTE, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
candle_15MINUTE['timestamp'] = pd.to_datetime(candle_15MINUTE['timestamp'], unit='ms')

candle_1HOUR = pd.DataFrame(candle_1HOUR, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
candle_1HOUR['timestamp'] = pd.to_datetime(candle_1HOUR['timestamp'], unit='ms')

candle_4HOUR = pd.DataFrame(candle_4HOUR, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
candle_4HOUR['timestamp'] = pd.to_datetime(candle_4HOUR['timestamp'], unit='ms')

candle_1DAY = pd.DataFrame(candle_1DAY, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
candle_1DAY['timestamp'] = pd.to_datetime(candle_1DAY['timestamp'], unit='ms')

candle_1WEEK = pd.DataFrame(candle_1WEEK, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
candle_1WEEK['timestamp'] = pd.to_datetime(candle_1WEEK['timestamp'], unit='ms')

# DEFINE VARIABLES
dates = []
prices = []
candles = []
dates_1W = []
prices_1W = []
dates_1D = []
prices_1D = []
dates_4H = []
prices_4H = []
dates_1H = []
prices_1H = []
dates_15M = []
prices_15M = []
dates_5M = []
prices_5M = []
dates_1M = []
prices_1M = []
i = 1
df = []
current_close = 1
current_timestamp = ""

# 1W/1D/4H...ECC CLOSES INFO
for i in candle_1WEEK.index:
    current_timestamp = candle_1WEEK.timestamp.values[i]
    current_close = int(float(candle_1WEEK.close.values[i]))

    dates_1W.append(current_timestamp)
    prices_1W.append(current_close)

for i in candle_1DAY.index:
    current_timestamp = candle_1DAY.timestamp.values[i]
    current_close = int(float(candle_1DAY.close.values[i]))

    dates_1D.append(current_timestamp)
    prices_1D.append(current_close)

for i in candle_4HOUR.index:
    current_timestamp = candle_4HOUR.timestamp.values[i]
    current_close = int(float(candle_4HOUR.close.values[i]))

    dates_4H.append(current_timestamp)
    prices_4H.append(current_close)

for i in candle_1HOUR.index:
    current_timestamp = candle_1HOUR.timestamp.values[i]
    current_close = int(float(candle_1HOUR.close.values[i]))

    dates_1H.append(current_timestamp)
    prices_1H.append(current_close)

for i in candle_15MINUTE.index:
    current_timestamp = candle_15MINUTE.timestamp.values[i]
    current_close = int(float(candle_15MINUTE.close.values[i]))

    dates_15M.append(current_timestamp)
    prices_15M.append(current_close)

for i in candle_5MINUTE.index:
    current_timestamp = candle_5MINUTE.timestamp.values[i]
    current_close = int(float(candle_5MINUTE.close.values[i]))

    dates_5M.append(current_timestamp)
    prices_5M.append(current_close)

for i in candle_1MINUTE.index:
    current_timestamp = candle_1MINUTE.timestamp.values[i]
    current_close = int(float(candle_1MINUTE.close.values[i]))

    dates_1M.append(current_timestamp)
    prices_1M.append(current_close)

#__________________________________________
#-----------MOVING AVERAGES----------------
#__________________________________________

#O GET DATES TO CALCULATE MOVING AVERAGE
def GET_DATES (prices, candles, periods):
    total_interactions = []
    k=1

    max_range=len(prices)
    min_range=len(prices)-periods

    for k in reversed(range(max_range)):
        current_timestamp = candles.timestamp.values[k]
        total_interactions.append(current_timestamp)

        max_range=max_range-1
        min_range=min_range-1

        if min_range <= periods:
            break

    prices=[]
    candles =[]
    return total_interactions


#-----------MEDIUM AVERAGE N PERIODS-------

def MEDIUM_AVERAGE (prices, candles, periods):
    MOVING_AVERAGE = []
    sum_close=0
    medium_average=0
    j=1
    iter = 0

    max_range=len(prices)
    min_range=len(prices)-periods

    for k in reversed(range(max_range)):
        for j in reversed(range(min_range, max_range)):
            iter = iter + 1

            current_close = int(float(candles.close.values[j]))
            sum_close = sum_close+current_close

        medium_average=sum_close/iter
        MOVING_AVERAGE.append(medium_average)
        iter=0
        sum_close=0
        medium_average=0
        max_range=max_range-1
        min_range=min_range-1

        if min_range <= periods:
            break

    prices=[]
    candles =[]
    return MOVING_AVERAGE

#------------------PLOT MEDIUM AVERAGE 1 DAY--------------------------

fig, axs = plt.subplots(2, 3)

axs[0, 0].plot(dates_1D, prices_1D, "-", linestyle='solid', marker='o', markersize=1, color="black")
media_local = MEDIUM_AVERAGE(prices_1D, candle_1DAY, 7)
data_local = GET_DATES(prices_1D, candle_1DAY, 7)
axs[0, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="magenta")

media_local = MEDIUM_AVERAGE(prices_1D, candle_1DAY, 14)
data_local = GET_DATES(prices_1D, candle_1DAY, 14)
axs[0, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="blue")

media_local = MEDIUM_AVERAGE(prices_1D, candle_1DAY, 21)
data_local = GET_DATES(prices_1D, candle_1DAY, 21)
axs[0, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="cyan")

media_local = MEDIUM_AVERAGE(prices_1D, candle_1DAY, 50)
data_local = GET_DATES(prices_1D, candle_1DAY, 50)
axs[0, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="green")

media_local = MEDIUM_AVERAGE(prices_1D, candle_1DAY, 100)
data_local = GET_DATES(prices_1D, candle_1DAY, 100)
axs[0, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="yellow")

media_local = MEDIUM_AVERAGE(prices_1D, candle_1DAY, 150)
data_local = GET_DATES(prices_1D, candle_1DAY, 150)
axs[0, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="orange")

media_local = MEDIUM_AVERAGE(prices_1D, candle_1DAY, 200)
data_local = GET_DATES(prices_1D, candle_1DAY, 200)
axs[0, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="red")

axs[0, 0].set_title(symbol + ' | BINANCE | 1D')

#---------------------PLOT MEDIUM AVERAGE 4H-----------------------

axs[0, 1].plot(dates_4H, prices_4H, "-", linestyle='solid', marker='o', markersize=1, color="black")
media_local = MEDIUM_AVERAGE(prices_4H, candle_4HOUR, 7)
data_local = GET_DATES(prices_4H, candle_4HOUR, 7)
axs[0, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="magenta")

media_local = MEDIUM_AVERAGE(prices_4H, candle_4HOUR, 14)
data_local = GET_DATES(prices_4H, candle_4HOUR, 14)
axs[0, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="blue")

media_local = MEDIUM_AVERAGE(prices_4H, candle_4HOUR, 21)
data_local = GET_DATES(prices_4H, candle_4HOUR, 21)
axs[0, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="cyan")

media_local = MEDIUM_AVERAGE(prices_4H, candle_4HOUR, 50)
data_local = GET_DATES(prices_4H, candle_4HOUR, 50)
axs[0, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="green")

media_local = MEDIUM_AVERAGE(prices_4H, candle_4HOUR, 100)
data_local = GET_DATES(prices_4H, candle_4HOUR, 100)
axs[0, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="yellow")

media_local = MEDIUM_AVERAGE(prices_4H, candle_4HOUR, 150)
data_local = GET_DATES(prices_4H, candle_4HOUR, 150)
axs[0, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="orange")

media_local = MEDIUM_AVERAGE(prices_4H, candle_4HOUR, 200)
data_local = GET_DATES(prices_4H, candle_4HOUR, 200)
axs[0, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="red")

axs[0, 1].set_title(symbol + ' | BINANCE | 4H')

#---------------------PLOT MOVING AVERAGE 1H------------------------

axs[0, 2].plot(dates_1H, prices_1H, "-", linestyle='solid', marker='o', markersize=1, color="black")
media_local = MEDIUM_AVERAGE(prices_1H, candle_1HOUR, 7)
data_local = GET_DATES(prices_1H, candle_1HOUR, 7)
axs[0, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="magenta")

media_local = MEDIUM_AVERAGE(prices_1H, candle_1HOUR, 14)
data_local = GET_DATES(prices_1H, candle_1HOUR, 14)
axs[0, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="blue")

media_local = MEDIUM_AVERAGE(prices_1H, candle_1HOUR, 21)
data_local = GET_DATES(prices_1H, candle_1HOUR, 21)
axs[0, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="cyan")

media_local = MEDIUM_AVERAGE(prices_1H, candle_1HOUR, 50)
data_local = GET_DATES(prices_1H, candle_1HOUR, 50)
axs[0, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="green")

media_local = MEDIUM_AVERAGE(prices_1H, candle_1HOUR, 100)
data_local = GET_DATES(prices_1H, candle_1HOUR, 100)
axs[0, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="yellow")

media_local = MEDIUM_AVERAGE(prices_1H, candle_1HOUR, 150)
data_local = GET_DATES(prices_1H, candle_1HOUR, 150)
axs[0, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="orange")

media_local = MEDIUM_AVERAGE(prices_1H, candle_1HOUR, 200)
data_local = GET_DATES(prices_1H, candle_1HOUR, 200)
axs[0, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="red")

axs[0, 2].set_title(symbol + ' | BINANCE | 1H')

#------------------PLOT MEDIUM AVERAGE 15 MIN--------------------------

axs[1, 0].plot(dates_15M, prices_15M, "-", linestyle='solid', marker='o', markersize=1, color="black")
media_local = MEDIUM_AVERAGE(prices_15M, candle_15MINUTE, 7)
data_local = GET_DATES(prices_15M, candle_15MINUTE, 7)
axs[1, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="magenta")

media_local = MEDIUM_AVERAGE(prices_15M, candle_15MINUTE, 14)
data_local = GET_DATES(prices_15M , candle_15MINUTE, 14)
axs[1, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="blue")

media_local = MEDIUM_AVERAGE(prices_15M, candle_15MINUTE, 21)
data_local = GET_DATES(prices_15M, candle_15MINUTE, 21)
axs[1, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="cyan")

media_local = MEDIUM_AVERAGE(prices_15M, candle_15MINUTE, 50)
data_local = GET_DATES(prices_15M, candle_15MINUTE, 50)
axs[1, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="green")

media_local = MEDIUM_AVERAGE(prices_15M, candle_15MINUTE, 100)
data_local = GET_DATES(prices_15M, candle_15MINUTE, 100)
axs[1, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="yellow")

media_local = MEDIUM_AVERAGE(prices_15M, candle_15MINUTE, 150)
data_local = GET_DATES(prices_15M, candle_15MINUTE, 150)
axs[1, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="orange")

media_local = MEDIUM_AVERAGE(prices_15M, candle_15MINUTE, 200)
data_local = GET_DATES(prices_15M, candle_15MINUTE, 200)
axs[1, 0].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="red")

axs[1, 0].set_title(symbol + ' | BINANCE | 15Min')

#--------------------PLOT MOVING AVERAGE 5M-------------------------

axs[1, 1].plot(dates_5M, prices_5M, "-", linestyle='solid', marker='o', markersize=1, color="black")
media_local = MEDIUM_AVERAGE(prices_5M, candle_5MINUTE, 7)
data_local = GET_DATES(prices_5M, candle_5MINUTE, 7)
axs[1, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="magenta")

media_local = MEDIUM_AVERAGE(prices_5M, candle_5MINUTE, 14)
data_local = GET_DATES(prices_5M, candle_5MINUTE, 14)
axs[1, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="blue")

media_local = MEDIUM_AVERAGE(prices_5M, candle_5MINUTE, 21)
data_local = GET_DATES(prices_5M, candle_5MINUTE, 21)
axs[1, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="cyan")

media_local = MEDIUM_AVERAGE(prices_5M, candle_5MINUTE, 50)
data_local = GET_DATES(prices_5M, candle_5MINUTE, 50)
axs[1, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="green")

media_local = MEDIUM_AVERAGE(prices_5M, candle_5MINUTE, 100)
data_local = GET_DATES(prices_5M, candle_5MINUTE, 100)
axs[1, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="yellow")

media_local = MEDIUM_AVERAGE(prices_5M, candle_5MINUTE, 150)
data_local = GET_DATES(prices_5M, candle_5MINUTE, 150)
axs[1, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="orange")

media_local = MEDIUM_AVERAGE(prices_5M, candle_5MINUTE, 200)
data_local = GET_DATES(prices_5M, candle_5MINUTE, 200)
axs[1, 1].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="red")

axs[1, 1].set_title(symbol + ' | BINANCE | 5Min')

#--------------------PLOT MOVING AVERAGE 1M-------------------------

axs[1, 2].plot(dates_1M, prices_1M, "-", linestyle='solid', marker='o', markersize=1, color="black")
media_local = MEDIUM_AVERAGE(prices_1M, candle_1MINUTE, 7)
data_local = GET_DATES(prices_1M, candle_1MINUTE, 7)
axs[1, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="magenta")

media_local = MEDIUM_AVERAGE(prices_1M, candle_1MINUTE, 14)
data_local = GET_DATES(prices_1M, candle_1MINUTE, 14)
axs[1, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="blue")

media_local = MEDIUM_AVERAGE(prices_1M, candle_1MINUTE, 21)
data_local = GET_DATES(prices_1M, candle_1MINUTE, 21)
axs[1, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="cyan")

media_local = MEDIUM_AVERAGE(prices_1M, candle_1MINUTE, 50)
data_local = GET_DATES(prices_1M, candle_1MINUTE, 50)
axs[1, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="green")

media_local = MEDIUM_AVERAGE(prices_1M, candle_1MINUTE, 100)
data_local = GET_DATES(prices_1M, candle_1MINUTE, 100)
axs[1, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="yellow")

media_local = MEDIUM_AVERAGE(prices_1M, candle_1MINUTE, 150)
data_local = GET_DATES(prices_1M, candle_1MINUTE, 150)
axs[1, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="orange")

media_local = MEDIUM_AVERAGE(prices_1M, candle_1MINUTE, 200)
data_local = GET_DATES(prices_1M, candle_1MINUTE, 200)
axs[1, 2].plot(data_local, media_local,  "-", linestyle='solid', alpha=0.4, marker='o', markersize=0.5, color="red")

axs[1, 2].set_title(symbol + ' | BINANCE | 1Min')

# RENAME X AND Y; THEN FIX OVERLAP ON DATES 
for ax in axs.flat:
    ax.set(xlabel='Time', ylabel='Price')

ax.xaxis_date()
fig.autofmt_xdate()
   
plt.xlabel("Time")
plt.ylabel('Price')

#MOSTRA IL GRAFICO
plt.show()

print("END")

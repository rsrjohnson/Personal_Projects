import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import requests
import json

import plotly.graph_objects as go

import datetime

from datetime import timedelta

from coinpaprika import client as Coinpaprika

client = Coinpaprika.Client()

start_date = datetime.date(2021, 8 , 31) #yyyy-d-m
number_of_days = (datetime.date.today()-start_date).days

candles_data={'data':[]}

for i in range(number_of_days):
    date=(start_date + datetime.timedelta(days = i)).isoformat()
    candles_data['data'].append(client.candles("btc-bitcoin", start=date)[0])

df_candles = pd.json_normalize(candles_data['data'])

fig = go.Figure(data=[go.Candlestick(x=df_candles['time_open'],
                open=df_candles['open'],
                high=df_candles['high'],
                low=df_candles['low'],
                close=df_candles['close'])])

fig.write_image("figure.png", engine="kaleido")
fig.write_html("figure.html")
#fig.show()
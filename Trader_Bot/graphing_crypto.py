import pandas as pd
import numpy as np
import requests
import json
import plotly.graph_objects as go
from datetime import datetime

#url = "http://api.coincap.io/v2/assets"
url="http://api.coincap.io/v2/candles?exchange=poloniex&interval=h8&baseId=ethereum&quoteId=bitcoin"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)


df = pd.json_normalize(data['data']) #Results contain the required data
print(df)




fig = go.Figure(data=[go.Candlestick(x=df['period'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

fig.show()
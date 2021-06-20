import urllib.request
import ssl
import json
import time

import pandas
import pandas as pd

api_key = 'owmitfizatgtqpey2ek1s'

coin_list = [
    "LTC",
    "ETH",
    "BTC"
]


#coins = ','.join(coin_list)

mp = [
    {"name": ""},
    {"symbol": ""},
    {"percent_change_24h": " - 24 Hour Percent Change: "},
    {"market_cap": " Market Cap: "},
    {"volume_24h_rank": " 24 Hour Volume Rank: "},
    {"url_shares": " URL Shares: "},
    {"reddit_posts": " Reddit Posts: "},
    {"tweets": " Tweets: "},
    {"galaxy_score": " Galaxy Score: "},
    {"volatility": " Volatility: "},
    #{"social_volume": " Social Volume: "},
    {"average_sentiment": "Average Sentiment"},
    {"news": " News: "},
    {"open": "Open"},
    {"high": "High"},
    {"low": "low"},
    {"close": " Close: "},
    {'time': ' Time:'},
]

feature_map = [
    {"percent_change_24h": " - 24 Hour Percent Change: "},
    {"market_cap": " Market Cap: "},
    {"volume_24h_rank": " 24 Hour Volume Rank: "},
    {"url_shares": " URL Shares: "},
    {"reddit_posts": " Reddit Posts: "},
    {"tweets": " Tweets: "},
    {"galaxy_score": " Galaxy Score: "},
    {"volatility": " Volatility: "},
    #{"social_volume": " Social Volume: "},
    {"average_sentiment": "Average Sentiment"},
    {"news": " News: "},
    {"open": "Open"},
    {"high": "High"},
    {"low": "low"},
    {"close": " Close: "},
    {'time': ' Time:'},
]

map_to_fields = ','.join(list(mp[attr].keys())[0] for attr in range(len(mp)))
feat_map_to_feat_fields = [list(key.keys())[0] for key in feature_map]

def get_data(l, u):
    #Starts from 1 September 2018
    url = "https://api.lunarcrush.com/v2?data=assets&key=" + api_key + "&symbol=" + coin_list[2] + \
          "&start=" + str(l) + '&to=' + str(u) +\
          "&interval=day&&time_series_indicators=" + map_to_fields + "&indicators=timeSeries"




    fields = [list(key.keys())[0] for key in mp]
    coins_df = pandas.DataFrame(columns=feat_map_to_feat_fields)


    assets = json.loads(urllib.request.urlopen(url).read())


    dat = assets['data'][0]['timeSeries']
    day = 0
    for day_dict in dat:
        if day != 0:
            required_data = [{ft: day_dict[ft] for ft in feat_map_to_feat_fields}]
            coins_df = coins_df.append(required_data, ignore_index=True)

        day += 1

    coins_df['time'] = pandas.to_datetime(coins_df['time'], unit='s')
    print(coins_df)

    return coins_df


###Loop until get all data#########
low_timestamp = 1537390800
upper_timestamp = low_timestamp + 864000
data = get_data(low_timestamp, upper_timestamp)

while upper_timestamp <= 1619384400:

    new_unix_timestamp = int((pd.to_datetime([str(data.iloc[-1]['time'])]).astype(int) / (10**9)).item())
    if new_unix_timestamp == low_timestamp:
        break

    low_timestamp = new_unix_timestamp
    upper_timestamp = low_timestamp + 864000
    print(low_timestamp)

    new_data = get_data(low_timestamp, upper_timestamp)
    data = data.append(new_data, ignore_index=True)

data.to_csv('cryptodata_lunarcrash.csv')

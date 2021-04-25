import urllib.request
import ssl
import json
import time

import pandas

api_key = '61wdf8bjzzq7kvrfin2l2c'

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
    {"social_volume": " Social Volume: "},
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
    {"social_volume": " Social Volume: "},
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

#Starts from 1 September 2018
url = "https://api.lunarcrush.com/v2?data=assets&key=" + api_key + "&symbol=" + coin_list[2] + "&data_points=900&interval=day"

      #"https://api.lunarcrush.com/v2?data=assets&key=" + api_key + "&symbol=" + coin_list[2] + \
      #"&start=1535749200&to=1619125200" + \
      #"&interval=day&&time_series_indicators=" + map_to_fields + "&indicators=timeSeries"



fields = [list(key.keys())[0] for key in mp]
coins_df = pandas.DataFrame(columns=feat_map_to_feat_fields)


assets = json.loads(urllib.request.urlopen(url).read())


data = assets['data'][0]['timeSeries']
day = 0
for day_dict in data:
    if day != 0:
        required_data = [{ft: day_dict[ft] for ft in feat_map_to_feat_fields}]
        coins_df = coins_df.append(required_data, ignore_index=True)

    day += 1

coins_df['time'] = pandas.to_datetime(coins_df['time'], unit='s')
print(coins_df)

###Test change
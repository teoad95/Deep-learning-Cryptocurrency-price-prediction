import json
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cryptocompare

requested_coin = 'ADA'
to_type = 'USD'
cryptos_list = cryptocompare.get_coin_list(format=False)
id_requested_coin = cryptos_list[requested_coin]['Id']

key = 'dc25ed2a142a694ce8caab2e1ead44b2c935edeed773973680ccea4016ecf60b'
endpoint = 'https://min-api.cryptocompare.com/data/social/coin/histo/day'
res = requests.get(endpoint+'?coinId=' + id_requested_coin + '&limit=2000&api_key=' + key)

coins_df = pd.DataFrame(json.loads(res.content)['Data'])
coins_df['time'] = pd.to_datetime(coins_df['time'], unit='s')

coins_df.to_csv(requested_coin + '-' + to_type + '.csv')
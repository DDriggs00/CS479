import requests
import json

apiKey = "UbqRLevtbDBHR8pxwGbk"
numCryptos = 100
url = "https://min-api.cryptocompare.com/data/histohour"

payload = {
    "fsym": "BTC",
    "tsym": "USD"
}

headers = {
    "authorization": "Apikey " + apiKey
}

result = requests.get(url, headers=headers, params=payload).json()

print(result)

coins = ['BTC','ETH','EOS','LTC','BCH','XRP','TRX','NEO','ETC','ZEC']
for coin in coins:
    btc = getHistoricalDataDaily(coin, all=True)
    with open(coin + '.csv', 'w') as f:  # Just use 'w' mode in 3.x
        row1 = btc[0]
        w = csv.DictWriter(f, row1.keys())
        w.writeheader()
        for row in btc:
            w.writerow(row)
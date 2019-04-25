import requests

# Get API key
# ApiKey.txt contians only a CryptoCompare API Key
apiKeyFile = open('apiKey.txt', 'r')
apiKey = content = apiKeyFile.read()
apiKeyFile.close()

numCryptos = 100
headers = {
    "authorization": "Apikey " + apiKey
}

# Given a positive integer n, returns the top n bitcoins in terms of market cap
def getTopCryptos(n = 10):
    if n >= 10:
        limit = n
    else:
        limit = 10
    url = 'https://min-api.cryptocompare.com/data/top/mktcap'
    payload = {
        "limit": limit,
        "tsym": "USD"
    }
    topCryptos = requests.get(url, headers=headers, params=payload).json()
    topCryptos = topCryptos["Data"]
    coins = []
    i = 0
    for coin in topCryptos:
        if i >= n:
            break
        info = coin["CoinInfo"]
        coins.append(info['Name'])
        i += 1
    return coins

def getHistoricalDataDaily(coin, numDays = 30, all = False):
    url = "https://min-api.cryptocompare.com/data/histoday"
    payload = {
        "fsym": coin,
        "tsym": "USD"
    }
    if all:
        payload['allData'] = "true"
    else:
        payload['limit'] = numDays
    histoDay =  requests.get(url, headers=headers, params=payload).json()
    return histoDay['Data']

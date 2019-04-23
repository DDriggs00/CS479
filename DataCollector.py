import requests
import json

# Get API key
# ApiKey.txt contians only a CryptoCompare API Key
apiKeyFile = open('apiKey.txt', 'r')
apiKey = content = apiKeyFile.read()
apiKeyFile.close()

numCryptos = 100
headers = {
    "authorization": "Apikey " + apiKey
}

def getTopCryptos(n):
    url = 'https://min-api.cryptocompare.com/data/top/mktcap'
    payload = {
        "limit": n,
        "tsym": "USD"
    }
    return requests.get(url, headers=headers, params=payload).json()

def getHistoricalDataDaily(numDays, coin):
    url = "https://min-api.cryptocompare.com/data/histoday"
    payload = {
        "fsym": coin,
        "tsym": "USD"
    }
    return requests.get(url, headers=headers, params=payload).json()

def getHistoricalDataHourly(numHours, coin):
    url = "https://min-api.cryptocompare.com/data/histohour"
    payload = {
        "fsym": coin,
        "tsym": "USD"
    }
    return requests.get(url, headers=headers, params=payload).json()



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
import requests
import json

apiKey = "018cc076c7cda28e5f823ef3ecf21bb5bfb086b0d13939491afcbfc8da8d575f"

url = "https://min-api.cryptocompare.com/data/price"

payload = {
    "fsym": "BTC",
    "tsyms": "USD"
}

headers = {
    "authorization": "Apikey " + apiKey
}

result = requests.get(url, headers=headers, params=payload).json()

print(result)
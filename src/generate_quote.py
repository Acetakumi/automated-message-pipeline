import requests
from config import Config

config = Config()

def get_romantic_quote():
    url = "https://api.api-ninjas.com/v2/quoteoftheday"

    headers = {
        "X-Api-Key": config.ninja_api_key
    }

    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.text)
    data = response.json()
    print(data)

    quote = f"{data[0]['quote']} - {data[0]['author']}"

    return quote
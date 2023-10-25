import requests
import json

try:
    results = requests.get("https://api.chucknorris.io/jokes/random")
    if results.status_code == 200:
        json_result = results.json()
        print(json_result["value"])
except requests.exceptions.RequestException as e:
    print("Could not do because of:")
    print(e)

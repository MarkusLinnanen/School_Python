import requests
import json
from geopy.geocoders import Nominatim

app = Nominatim(user_agent="tutorial")
iput = input("Input location: ")
location = app.geocode(iput)
if location is not None:
    rawloc = location.raw
    getstring = f"https://api.openweathermap.org/data/2.5/weather?lat={rawloc['lat']}&lon={rawloc['lon']}&exclude=minutely,horly,daily,alerts&units=metric&appid=6e845d0e04bb10abda9c8b13da73f29c"
    print(getstring)
    try:
        results = requests.get(getstring)
        if results.status_code == 200:
            json_result = results.json()
            print("the weather is " + json_result["weather"][0]["main"], "\n"+"temprature is", str(json_result["main"]["temp"]), "⁰C")
    except requests.exceptions.RequestException as e:
        print("Could not do because of:")
        print(e)
else:
    print("Input insufficient")

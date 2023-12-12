# openweathermap.org exposes APIs for reading the weather data from various cities.
# The documentation is at https://openweathermap.org/guide#how
# 1. Use the below weather end-point to get the current weather details of Hyderabad
# http://api.openweathermap.org/data/2.5/weather?q=hyderabad&appid={your_key}
import requests
from dotenv import dotenv_values

env_dict = dotenv_values(".env")
appid = env_dict["API_KEY"]
print(appid)
url = "http://api.openweathermap.org/data/2.5/weather"

params = {"q": "hyderabad", "appid": appid}

resp = requests.get(url,params=params)
assert resp.status_code == 200

lat = resp.json()["coord"]["lat"]
lon = resp.json()["coord"]["lon"]

assert resp.json()['name'] == 'Hyderabad'
#
# 2. Use the coordinates (longitude and latitude) of of the above response to the end-point
# http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={your_key}

params = {"lat": lat, "lon": lon, "appid": appid}

resp = requests.get(url, params=params)
print(resp.url)
print(resp.json())
# and verify the below in response
# - name --> Hyderabad
assert resp.json()['name'] == 'Hyderabad'
# - sys.country --> IN
assert resp.json()['sys']['country']=='IN'
# - main.temp_min --> greater than 0
assert resp.json()['main']['temp_min'] >0
# - main.temp --> greater than 0
assert resp.json()['main']['temp'] >0
# Hint:
# - You need to register in the application and get your API key as mentioned here in your API requests"
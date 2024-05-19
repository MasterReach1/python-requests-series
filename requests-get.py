import os
import json
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")

city = "Dallas"
state = "TX"
country = "US"

limit = 5

request = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={API_KEY}")

if request.status_code == 200:
    data = request.json()
else:
    data = []

latitude = data[0].get('lat')
longitude = data[0].get('lon')

# weather data latitude and longitude

weatherRequest = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}")

if request.status_code == 200:
    data = weatherRequest.json()
else:
    data = {}

weatherData = data.get("main")
print(weatherData.get("temp"))
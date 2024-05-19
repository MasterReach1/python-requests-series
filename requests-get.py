import json
import requests

API_KEY = "efac550a3554d8fe000295cd0666b5b9"

city = "Dallas"
state = "TX"
country = "US"
limit = 5

r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={API_KEY}")

if r.status_code == 200:
    data = r.json()
else:
    data = ""

latitude = data[0].get('lat')
longitude = data[0].get('lon')

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}")

#access the data retrieved with the proper commands
#api docs in description

weatherdata = r.json()

weatherData = weatherdata.get('weather', {})


print(weatherData[0].get('description'))
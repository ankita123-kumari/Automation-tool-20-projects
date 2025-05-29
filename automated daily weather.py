import requests

API_KEY = "your_openweather_api_key"
CITY = "Auckland"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    response = requests.get(URL)
    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"Today's weather in {CITY}: {temp}°C, {description}")

get_weather()
import requests
import json

city = input("Enter a city name: ")

api_key = "607f24073699dcab4fa4f1b1cf2eb885"
base_url = "https://api.openweathermap.org/data/2.5/weather"

A={
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(base_url,A)
data = response.json()

def display_weather(city):
    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    feelslike = data["main"]["feels_like"]
    wind_speed = data["wind"]["speed"]
    desc = data["weather"][0]["description"]
    print(f"City name: {city_name.upper()}")
    print(f"Country Code: {country.upper()}")
    print(f"Temperature: {temperature} C")
    print(f"Feels Like: {feelslike} C")
    print(f"Wind Speed: {wind_speed}")
    print(f"Weather Description: {desc.upper()}")

display_weather(city)








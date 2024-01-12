import requests
import json
#Enter city name part with error handling for invalid city name

while True:
    city = input("Enter city name: ")

    api_key = "607f24073699dcab4fa4f1b1cf2eb885"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    A={
    "q": city,
    "appid": api_key,
    "units": "metric"
    }
    #gets data from the API
    response = requests.get(base_url,A)
    data = response.json()
    #Prints all of the info of the JSON provided by API(Used for checking purposes)
    if data["cod"] == "404":
        print("Please enter a valid city name")
        continue
    else:
        break
 #Prints all of the info of the JSON provided by API(Used for checking purposes)

#print(json.dumps(data,indent=3))

#displays weather information
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

def recommendation_input():
    while True:
        recommendation = str(input("Do you want recommendations?Type(Y or N): ")).upper()
        if recommendation == "Y":
            return recommendation
        elif recommendation == "N":
            return recommendation
        else:
            continue

def recommendation_display():
        if data["wind"]["speed"]>= 8:
            print("Caution high wind speeds")
        elif data["wind"]["speed"] <= 6:
            print("Good day to wear a hat")
display_weather(city)
rec_input = recommendation_input()
if rec_input == "N":
    print("Congrats")
elif rec_input == "Y":
    (recommendation_display())






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

print(json.dumps(data,indent=3))

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

def recommendation_display():
    if data["wind"]["speed"].values()>= 8:
        print("Not a good day to wear a hat")
    elif data["wind"]["speed"] <= 6:
        print("Good day to wear a hat")
    elif data["main"]["temp"] >= 26:
        print("Should be sunny remember to put on sun screen for outdoor activities")
    elif data["main"]["temp"] <= 25:
        print("Should be good even without sun screen for outdoor activities")
def recommendation_input():
    detector = 0
    while detector == 0:
        recommendation = input("Do you want recommendations?Type(Y or N): ")

        if recommendation == 'N' or 'n':
            detector = 1
        elif recommendation == 'Y' or 'y':
            print(recommendation_display())
        else:

            print("Please type in a valid response")
            detector = 0

display_weather(city)

recommendation_input()









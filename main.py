import requests
import json

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = json.loads(response.text)

        # Extract relevant information from the response
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]

        # Print the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching weather data:", e)

# Provide your API key
api_key = "3d32c800285f499e54595ae6ae1461de"

while True:
    # Ask the user to input the city name
    city_name = input("Enter the city name (or 'q' to quit): ")

    if city_name.lower() == "q":
        break

    # Call the function to get and display the weather information
    get_weather(api_key, city_name)

    # Prompt the user to test again or quit
    user_choice = input("Press Enter to test again or 'q' to quit: ")
    if user_choice.lower() == "q":
        break


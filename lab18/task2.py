import requests
import json
def get_weather():
    api_key = input("Enter your OpenWeatherMap API key: ")
    city_name = input("Enter city name: ")
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json()
        # Save to JSON file
        filename = f"{city_name}_weather.json"
        with open(filename, 'w') as json_file:
            json.dump(weather_data, json_file, indent=4)
        print(f"\nWeather data saved to {filename}")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

# Run the function
get_weather()
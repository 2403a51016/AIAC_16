import requests
def display_weather(city_name, api_key):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Extract and format specific fields
        city = data.get('name', city_name)
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()
        print(f"\nCity: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
        else:
            print("Error: Could not connect to API. Check your API key or network connection.")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")
# Example usage:
# Replace 'your_api_key_here' with your actual OpenWeatherMap API key
display_weather("Paris", "d94954d62965729233e649b6e6637c79")
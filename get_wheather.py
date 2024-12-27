import requests
from speech import say

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

def get_location(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    location_data = response.json()
    return location_data['city'], location_data['region'], location_data['country']

def get_weather(city):
    api_key = '3e12d3dbfc1144cebc4113743242612'  # Replace with your WeatherAPI key
    weather_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    response = requests.get(weather_url)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def main():
    ip = get_ip()
    city, region, country = get_location(ip)
    weather_data = get_weather(city)
    
    if weather_data:
        location=(f" {city}, {region}, {country}")
        whether=(f" {weather_data['current']['condition']['text']}")
        temprature=(f" {weather_data['current']['temp_c']}°C")
        humidity=(f" {weather_data['current']['humidity']}%")
        windspeed=(f" {weather_data['current']['wind_kph']} kph")
        print(f"Sir your wheather is {whether} in {location} with {temprature} Temprature and {humidity} Hummidity and {windspeed} Wind Speed")
        say(f"Sir your wheather is {whether} in {location} with {temprature} Temprature and {humidity} Hummidity and {windspeed} Wind Speed")
    else:
        print("Failed to retrieve weather data")


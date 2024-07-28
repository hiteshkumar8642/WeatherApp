import requests
import time
from datetime import datetime
from django.core.management.base import BaseCommand
from weather.models import City, WeatherData

API_KEY = '24676a29610299893ad52470dd557f7f'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fetch_weather_data(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    return {
        'main': data['weather'][0]['main'],
        'temp': kelvin_to_celsius(data['main']['temp']),
        'feels_like': kelvin_to_celsius(data['main']['feels_like']),
        'dt': datetime.fromtimestamp(data['dt'])
    }

class Command(BaseCommand):
    help = 'Fetch weather data'

    def handle(self, *args, **kwargs):
        cities = City.objects.all()
        for city in cities:
            weather_data = fetch_weather_data(city.name)
            WeatherData.objects.create(
                city=city,
                main=weather_data['main'],
                temp=weather_data['temp'],
                feels_like=weather_data['feels_like'],
                dt=weather_data['dt']
            )
        self.stdout.write(self.style.SUCCESS('Successfully fetched weather data'))

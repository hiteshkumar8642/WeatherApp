from django.test import TestCase
from .models import City, WeatherData
from .management.commands.fetch_weather import fetch_weather_data, kelvin_to_celsius

class WeatherDataTests(TestCase):
    def setUp(self):
        City.objects.create(name='Delhi')

    def test_kelvin_to_celsius(self):
        self.assertEqual(kelvin_to_celsius(300), 26.85)

    def test_fetch_weather_data(self):
        city = City.objects.get(name='Delhi')
        data = fetch_weather_data(city.name)
        self.assertIn('main', data)
        self.assertIn('temp', data)

    def test_daily_summary(self):
        city = City.objects.get(name='Delhi')
        WeatherData.objects.create(city=city, main='Clear', temp=30, feels_like=32, dt='2024-07-25T10:00:00Z')
        WeatherData.objects.create(city=city, main='Clear', temp=35, feels_like=37, dt='2024-07-25T15:00:00Z')
        summary = WeatherData.daily_summary(city)
        self.assertEqual(summary['avg_temp'], 32.5)
        self.assertEqual(summary['max_temp'], 35)
        self.assertEqual(summary['min_temp'], 30)
        self.assertEqual(summary['dominant_condition'], 'Clear')

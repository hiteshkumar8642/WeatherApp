from django.test import TestCase
from .models import City, WeatherData
from datetime import datetime
from .management.commands.fetch_weather import fetch_weather_data, kelvin_to_celsius

from django.utils import timezone
from django.test import TestCase
from .models import City, WeatherData
from datetime import datetime

class WeatherDataTests(TestCase):
    def setUp(self):
        self.city = City.objects.create(name='Delhi')
        today = timezone.now().date()
        # Use today's date for test data
        WeatherData.objects.create(
            city=self.city,
            main='Clear',
            temp=30.0,
            feels_like=32.0,
            dt=timezone.make_aware(datetime.combine(today, datetime.min.time()))
        )
        WeatherData.objects.create(
            city=self.city,
            main='Clear',
            temp=35.0,
            feels_like=37.0,
            dt=timezone.make_aware(datetime.combine(today, datetime.max.time()))
        )

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(300), 26.85, places=2)

    def test_fetch_weather_data(self):
        city = City.objects.get(name='Delhi')
        data = fetch_weather_data(city.name)
        self.assertIn('main', data)
        self.assertIn('temp', data)

    def test_daily_summary(self):
        summary = WeatherData.daily_summary(self.city)
        print("Summary:", summary)  # Debug output
        self.assertIsNotNone(summary, "Summary should not be None")
        self.assertAlmostEqual(summary['avg_temp'], 32.5, places=1)
        self.assertEqual(summary['max_temp'], 35)
        self.assertEqual(summary['min_temp'], 30)
        self.assertEqual(summary['dominant_condition'], 'Clear')

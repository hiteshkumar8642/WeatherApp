from django.utils import timezone
from django.db import models
from django.db.models import Avg, Max, Min, Count
from datetime import datetime

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    main = models.CharField(max_length=100)
    temp = models.FloatField()
    feels_like = models.FloatField()
    dt = models.DateTimeField()

    def __str__(self):
        return f'{self.city.name} - {self.dt}'

    @staticmethod
    def daily_summary(city):
        today = timezone.now().date()
        print(f"Today’s date: {today}")  # Debug output
        data = WeatherData.objects.filter(city=city, dt__date=today)
        print(f"Data count: {data.count()}")  # Debug output
        if not data.exists():
            return None

        avg_temp = data.aggregate(Avg('temp'))['temp__avg']
        max_temp = data.aggregate(Max('temp'))['temp__max']
        min_temp = data.aggregate(Min('temp'))['temp__min']

        dominant_condition = data.values('main').annotate(count=Count('main')).order_by('-count').first()
        dominant_condition = dominant_condition['main'] if dominant_condition else None

        return {
            'avg_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }

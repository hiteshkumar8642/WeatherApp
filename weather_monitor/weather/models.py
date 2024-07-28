from django.db import models

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
from django.db.models import Avg, Max, Min

class WeatherData(models.Model):
    ...
    @staticmethod
    def daily_summary(city):
        today = datetime.now().date()
        data = WeatherData.objects.filter(city=city, dt__date=today)
        if not data.exists():
            return None

        avg_temp = data.aggregate(Avg('temp'))['temp__avg']
        max_temp = data.aggregate(Max('temp'))['temp__max']
        min_temp = data.aggregate(Min('temp'))['temp__min']
        dominant_condition = data.values('main').annotate(count=models.Count('main')).order_by('-count')[0]['main']

        return {
            'avg_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }
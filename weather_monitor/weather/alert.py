from weather.models import WeatherData
from django.core.mail import send_mail

def check_alerts():
    cities = City.objects.all()
    for city in cities:
        data = WeatherData.objects.filter(city=city).order_by('-dt')[:2]
        if len(data) < 2:
            continue

        if data[0].temp > 35 and data[1].temp > 35:
            send_mail(
                'Temperature Alert',
                f'Temperature in {city.name} exceeded 35°C for two consecutive updates.',
                'from@example.com',
                ['to@example.com']
            )

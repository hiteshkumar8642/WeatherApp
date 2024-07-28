# Weather Monitoring System

## Overview

This Django project is a real-time data processing system for weather monitoring. It retrieves weather data from the OpenWeatherMap API, processes it to provide daily summaries, and supports alerting thresholds. 

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Installation](#installation)
- [Migrations](#migrations)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Example Usage](#example-usage)
- [Alerts](#alerts)
- [Contributing](#contributing)

# Prerequisites

Before setting up the environment, ensure you have the following installed:

- Python 3.8 or later
- pip (Python package installer)

# Setup

```bash
# Clone the Repository
https://github.com/hiteshkumar8642/WeatherApp.git
cd cd weather-monitoring

# Create a Virtual Environment
python -m venv venv

# Activate the Virtual Environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

# Installation
pip install -r requirements.txt

# Migrations
python manage.py migrate


# Running the Application
python manage.py runserver

# Running Tests
python manage.py test

# Example Usage
Fetch Weather Data
The system fetches weather data from the OpenWeatherMap API at a configurable interval. To test the functionality, ensure the scheduler is running (as configured in the tasks.py).

Daily Summary
To get the daily weather summary for a city, use the Django shell or your application’s interface:
```bash
from weather.models import City, WeatherData
from django.utils import timezone
from datetime import datetime

city = City.objects.create(name='Delhi')
WeatherData.objects.create(
    city=city,
    main='Clear',
    temp=30.0,
    feels_like=32.0,
    dt=timezone.make_aware(datetime.combine(timezone.now().date(), datetime.min.time()))
)
WeatherData.objects.create(
    city=city,
    main='Clear',
    temp=35.0,
    feels_like=37.0,
    dt=timezone.make_aware(datetime.combine(timezone.now().date(), datetime.max.time()))
)
summary = WeatherData.daily_summary(city)
print(summary)

```

# Alerts
Set up and configure alert thresholds based on your requirements. The system will notify you if the conditions exceed the configured thresholds.

## Contributing
```bash
#Fork the Repository
#Click the "Fork" button at the top right of the repository page.

#Clone Your Fork
https://github.com/hiteshkumar8642/WeatherApp.git

#Create a New Branch
git checkout -b feature/my-new-feature

#Make Changes
#Implement your changes or bug fixes.

#Commit Changes
git add .
git commit -m "Add a new feature or fix a bug"

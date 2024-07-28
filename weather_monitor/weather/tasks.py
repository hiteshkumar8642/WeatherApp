from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command

def fetch_weather():
    call_command('fetch_weather')

def check_alerts():
    # Import the check_alerts function here to avoid circular import issues
    from .alerts import check_alerts
    check_alerts()

def start():
    scheduler = BackgroundScheduler()
    # Schedule the fetch_weather command to run every 5 minutes
    scheduler.add_job(fetch_weather, 'interval', minutes=5)
    # Schedule the check_alerts function to run every 5 minutes
    scheduler.add_job(check_alerts, 'interval', minutes=5)
    scheduler.start()

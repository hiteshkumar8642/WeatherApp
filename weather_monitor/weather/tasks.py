from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(call_command, 'fetch_weather', trigger='interval', minutes=5)
    scheduler.add_job(check_alerts, trigger='interval', minutes=5)
    scheduler.start()

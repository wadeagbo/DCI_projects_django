import requests
from django.core.management.base import BaseCommand
from weather.models import Weather

import time as sleep_time


class Command(BaseCommand):
    help = "Stores the weather data"

    def handle(self, *args, **kwargs):

        while True:
            # Make an API request to get the weather data
            response = requests.get(
                "https://api.open-meteo.com/v1/forecast?latitude=51.45&longitude=11.97&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m",
                auth=("user", "pass"),
            )
            data = response.json()

            # Store the data in the Weather model

            temperature = data["current_weather"]["temperature"]
            windspeed = data["current_weather"]["windspeed"]
            time = data["current_weather"]["time"]

            Weather_info = Weather.objects.create(
                time=time, temperature=temperature, windspeed=windspeed
            )
            print("This is weather information now:", Weather_info)

            # Sleep for 5 minutes
            sleep_time.sleep(300)

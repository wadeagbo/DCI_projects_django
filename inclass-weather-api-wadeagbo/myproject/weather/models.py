from django.db import models
from django.utils import timezone


class Weather(models.Model):
    temperature = models.FloatField()

    time = models.DateTimeField(default=timezone.now)

    windspeed = models.FloatField()

    def __str__(self):
        return f" Time:  {self.time} ---  Temperature: {self.temperature}°C   ----   Windspeed:{self.windspeed}"

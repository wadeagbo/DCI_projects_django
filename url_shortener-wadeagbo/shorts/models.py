from django.db import models
import random
import string
import datetime

class ShortURL(models.Model):
    long_url = models.URLField(max_length=500)
    shortened = models.CharField(max_length=10, unique=True, blank=True)
    expiration_date = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=7))

    def __str__(self):
         return f"Expiry date: {self.expiration_date}    Short url:{self.shortened}    Long Url: {self.long_url}"


    def save(self, *args, **kwargs):
        if not self.shortened:
            self.shortened = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        super().save(*args, **kwargs)

from django.db import models
from django.contrib.auth.models import User


class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.DateField()
    user = models.ForeignKey(User, related_name="reminders", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

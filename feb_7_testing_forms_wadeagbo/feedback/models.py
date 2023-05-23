from django.db import models
from django.utils import timezone

# Create your models here.
class Feedback(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=500)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __repr__(self) -> str:
        return f"ID: {self.id}, {self.email}"

    def __str__(self) -> str:
        return f"ID: {self.id}, {self.email}"
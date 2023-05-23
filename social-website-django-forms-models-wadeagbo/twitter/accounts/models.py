from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        primary_key=True,
        verbose_name="user",
        related_name="profile",
        on_delete=models.CASCADE,
    )
    bio = models.TextField(max_length=255, blank=True, null=True)
    followers = models.ManyToManyField(User, blank=True, related_name="followers")

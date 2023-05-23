from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Reminder
from django.core.validators import MinLengthValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class ReminderSerializer(serializers.ModelSerializer):
    description = serializers.CharField(
        max_length=255, validators=[MinLengthValidator(10)]
    )
    user = UserSerializer()
    due_date = serializers.DateField(required=True)

    class Meta:
        model = Reminder
        fields = ("id", "title", "description", "user", "due_date")

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.get_or_create(**user_data)[0]
        reminder = Reminder.objects.create(user=user, **validated_data)
        return reminder

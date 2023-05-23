from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .models import Reminder
from .serializers import ReminderSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class PaginatedReminder(LimitOffsetPagination):
    default_limit = 5
    max_limit = 50


class ReminderList(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    # @swagger_auto_schema(
    #     operation_description="List all reminders for the current user",
    #     responses={
    #         200: ReminderSerializer(many=True),
    #         401: "Unauthorized",
    #     }
    # )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ReminderCreate(CreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class ReminderDetail(RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

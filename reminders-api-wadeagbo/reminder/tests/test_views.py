from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from reminder.models import Reminder
from reminder.serializers import UserSerializer, ReminderSerializer


class ReminderTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="testuser", password="testpass")
        self.reminder = Reminder.objects.create(
            title="Test Reminder",
            description="Test Reminder Description",
            user=self.user,
            due_date="2022-02-22",
        )
        self.url = reverse("reminder-detail", args=[self.reminder.id])

    def test_get_reminder_list(self):
        response = self.client.get(reverse("reminder-list"))
        reminders = Reminder.objects.all()
        self.assertEqual(len(response.data), len(reminders))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

 

    def test_create_reminder(self):
        data = {
        "title": "test title",
        "description": "test description",
        "due_date": "2022-12-31",
        "user": {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        }
    }

        response = self.client.post(reverse("reminder-list"), data=data, format='json') 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  
        self.assertEqual(Reminder.objects.count(), 1)
        self.assertEqual(Reminder.objects.get().title, "Test Reminder")




    def test_get_reminder_detail(self):
        response = self.client.get(self.url)
        serializer = ReminderSerializer(instance=self.reminder)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


 

    def test_update_reminder(self):
        reminder = Reminder.objects.create(
        title="test title",
        description="test description",
        due_date="2022-12-31",
        user=User.objects.create(username="testuserr", email="testuser@example.com")
    )
        data = {
        "title": "test title",
        "description": "test description",
        "due_date": "2022-11-31",
        "user": {
            "username": "testuser",
            "email": "testuser@example.com"
        }
    }
        response = self.client.put(reverse("reminder-detail", args=[reminder.id]), data=data, format='json')
        self.assertEqual(response.status_code, status. HTTP_400_BAD_REQUEST)  
        reminder.refresh_from_db()
        self.assertEqual(reminder.title, "test title")
        self.assertEqual(reminder.description, "test description")
        self.assertEqual(str(reminder.due_date), "2022-12-31")



    def test_delete_reminder(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reminder.objects.count(), 0)


class UserTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="testusery", password="testpass")
        self.url = reverse("user-detail", args=[self.user.id])

    def test_get_user_list(self):
        response = self.client.get(reverse("user-list"))
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        response = self.client.get(self.url)
        serializer = UserSerializer(instance=self.user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
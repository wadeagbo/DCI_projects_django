from django.test import TestCase
from datetime import date
from reminder.models import Reminder
from django.contrib.auth.models import User

class ReminderModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
            email="testuser@example.com"
        )
        self.reminder = Reminder.objects.create(
            title="Test Reminder",
            description="This is a test reminder",
            due_date=date.today(),
            user=self.user
        )

    def test_reminder_str_method(self):
        self.assertEqual(str(self.reminder), "Test Reminder")


    

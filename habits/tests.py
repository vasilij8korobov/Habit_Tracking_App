from django.test import TestCase
from rest_framework.test import APIClient
from users.models import User
from .models import Habit


class HabitTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        data = {
            'place': 'Дом',
            'time': '09:00:00',
            'action': 'Пить воду',
            'time_to_complete': 60,
        }
        response = self.client.post('/api/habits/', data)
        self.assertEqual(response.status_code, 201)

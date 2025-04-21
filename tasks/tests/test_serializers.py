from rest_framework.test import APITestCase
from tasks.serializers import TaskSerializer
from tasks.models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskSerializerTest(APITestCase):
    def test_due_date_validation(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        data = {
               "title": "Learn Python",
                "description": "Python is good language",
                "is_completed": True,
                "due_date": "2025-04-18"
        }
        serializer = TaskSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('due_date', serializer.errors)
from django.test import TestCase
from tasks.models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskModelTest(TestCase):
    def test_str_representation(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        task = Task.objects.create(title='Sample Task', owner=user)
        self.assertEqual(str(task), 'Sample Task')
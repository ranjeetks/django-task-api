from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class TaskViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.client.login(username='testuser', password='pass123')

    def test_user_registration(self):
        #url = reverse('users/register/')  # Update with your actual register path name
        url='/api/users/register/'
        data = {
                'email': "user11@example.com",
                'username': "user11",
                'full_name': "Hello user",
                'password': "ists@1234"
        }
        response = self.client.post(url, data)
        print("Status Code:", response.status_code)
        print("Response content:", response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
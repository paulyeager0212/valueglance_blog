from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class AuthTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass', email='testuser@example.com', first_name='Test', last_name='User')
        self.user.save()

    def test_register_user(self):
        url = reverse('user-register')
        data = {
            'username': 'newuser',
            'password': 'newpass',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['detail'], 'Registration successful.')

    def test_login_user(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_credentials(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'wrongpass'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'No active account found with the given credentials')

    def test_access_protected_endpoint_with_valid_token(self):
        login_url = reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        login_response = self.client.post(login_url, data, format='json')
        access_token = login_response.data['access']

        url = reverse('post-list-create')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_protected_endpoint_with_invalid_token(self):
        url = reverse('post-list-create')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer invalid_token')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_blog_post_without_authentication(self):
        url = reverse('post-list-create')
        data = {
            'title': 'Unauthorized Post',
            'content': 'This should fail.',
            'categories': []
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

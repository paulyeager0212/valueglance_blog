from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Post, Category

class BlogPostTests(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(
            username='testuser', password='testpassword',
            first_name='Test', last_name='User'
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))

        # Create a category
        self.category = Category.objects.create(name="Test Category")

    def test_register(self):
        url = reverse('user-register')
        data = {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        url = reverse('token_obtain_pair')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_refresh(self):
        url = reverse('token_refresh')
        refresh = str(RefreshToken.for_user(self.user))
        data = {'refresh': refresh}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_create_post(self):
        url = reverse('post-list-create')
        data = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'categories': [self.category.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_list_posts(self):
        Post.objects.create(
            title='Test Post', content='This is a test post content.', author=self.user
        )
        url = reverse('post-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Post')

    def test_retrieve_post(self):
        post = Post.objects.create(
            title='Test Post', content='This is a test post content.', author=self.user
        )
        url = reverse('post-detail', args=[post.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')

    def test_update_post(self):
        post = Post.objects.create(
            title='Test Post', content='This is a test post content.', author=self.user
        )
        url = reverse('post-detail', args=[post.id])
        data = {'title': 'Updated Post', 'content': 'This is updated content.'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, 'Updated Post')
        self.assertEqual(post.content, 'This is updated content.')

    def test_delete_post(self):
        post = Post.objects.create(
            title='Test Post', content='This is a test post content.', author=self.user
        )
        url = reverse('post-detail', args=[post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_create_post_unauthenticated(self):
        self.client.credentials()  # Remove the authentication token
        url = reverse('post-list-create')
        data = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'categories': [self.category.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_post_unauthenticated(self):
        post = Post.objects.create(
            title='Test Post', content='This is a test post content.', author=self.user
        )
        self.client.credentials()  # Remove the authentication token
        url = reverse('post-detail', args=[post.id])
        data = {'title': 'Updated Post', 'content': 'This is updated content.'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_post_unauthenticated(self):
        post = Post.objects.create(
            title='Test Post', content='This is a test post content.', author=self.user
        )
        self.client.credentials()  # Remove the authentication token
        url = reverse('post-detail', args=[post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

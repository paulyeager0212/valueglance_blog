from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Post, Category, Comment
from rest_framework_simplejwt.tokens import RefreshToken

class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = RefreshToken.for_user(self.user).access_token
        self.api_authentication()

        self.category = Category.objects.create(name='Category1')
        self.blog_post = Post.objects.create(
            title='Test Title',
            content='Test Content',
            author=self.user
        )
        self.blog_post.categories.add(self.category)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_blog_post(self):
        data = {
            'title': 'New Title',
            'content': 'New Content',
            'categories': [self.category.id]
        }
        response = self.client.post(reverse('post-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_blog_post_list(self):
        response = self.client.get(reverse('post-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_blog_post_detail(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.blog_post.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_blog_post(self):
        data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'categories': [self.category.id]
        }
        response = self.client.put(reverse('post-detail', kwargs={'pk': self.blog_post.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_blog_post(self):
        response = self.client.delete(reverse('post-detail', kwargs={'pk': self.blog_post.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_blog_post_unauthenticated(self):
        self.client.credentials()  # Remove authentication
        data = {
            'title': 'New Title',
            'content': 'New Content',
            'categories': [self.category.id]
        }
        response = self.client.post(reverse('post-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_blog_post_unauthenticated(self):
        self.client.credentials()  # Remove authentication
        data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'categories': [self.category.id]
        }
        response = self.client.put(reverse('post-detail', kwargs={'pk': self.blog_post.id}), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_blog_post_unauthenticated(self):
        self.client.credentials()  # Remove authentication
        response = self.client.delete(reverse('post-detail', kwargs={'pk': self.blog_post.id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_blog_post_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer invalid_token')  # Invalid token
        data = {
            'title': 'New Title',
            'content': 'New Content',
            'categories': [self.category.id]
        }
        response = self.client.post(reverse('post-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

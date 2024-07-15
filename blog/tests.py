from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Post
from rest_framework_simplejwt.tokens import RefreshToken

class BlogPostTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.obtain_token()

        self.blog_post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            author=self.user
        )

    def obtain_token(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_blog_post(self):
        url = reverse('post-list-create')
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Post')
        self.assertEqual(response.data['content'], 'New Content')
        self.assertEqual(response.data['author'], self.user.id)

    def test_get_blog_posts(self):
        url = reverse('post-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.blog_post.title)
        self.assertEqual(response.data[0]['content'], self.blog_post.content)

    def test_get_single_blog_post(self):
        url = reverse('post-detail', kwargs={'pk': self.blog_post.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.blog_post.title)
        self.assertEqual(response.data['content'], self.blog_post.content)

    def test_update_blog_post(self):
        url = reverse('post-detail', kwargs={'pk': self.blog_post.id})
        data = {'title': 'Updated Post', 'content': 'Updated Content'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Post')
        self.assertEqual(response.data['content'], 'Updated Content')

    def test_delete_blog_post(self):
        url = reverse('post-detail', kwargs={'pk': self.blog_post.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=self.blog_post.id).exists())

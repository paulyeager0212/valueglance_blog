from django.urls import path
from .views import PostListCreate, PostDetail, UserCreate

urlpatterns = [
  path('posts/', PostListCreate.as_view(), name='post-list-create'),
  path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
  path('register/', UserCreate.as_view(), name='user-register'),
]
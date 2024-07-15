from django.urls import path
from .views import PostListCreate, PostDetail, UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
  path('posts/', PostListCreate.as_view(), name='post-list-create'),
  path('posts/<int:pk>', PostDetail.as_view(), name='post-detail'),
  path('register/', UserCreate.as_view(), name='user-create'),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # To refresh JWT token
]
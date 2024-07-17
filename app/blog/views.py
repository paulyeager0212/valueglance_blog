from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import  IsAuthenticated
from .models import Post, Category
from .serializers import PostSerializer, UserSerializer, PostDetailSerializer
from django.contrib.auth.models import User

# Create your views here.
class PostListCreate(generics.ListCreateAPIView):
  queryset = Post.objects.all().select_related('author').prefetch_related('categories')
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all().select_related('author').prefetch_related('categories')
  serializer_class = PostDetailSerializer
  permission_classes = [IsAuthenticated]

class UserCreate(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def post(self, request, *args, **kwargs):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"detail": "Registration successful."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

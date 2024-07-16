from rest_framework import serializers
from .models import Post, Comment, Category
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
  """
  Serializer to represent the User model with essential fields.
  """
  class Meta:
    model = User
    fields = ['id', 'first_name', 'last_name', 'username', 'email']

class CategorySerializer(serializers.ModelSerializer):
  """
  Serializer to represent the Category model
  """
  class Meta:
    model = Category
    fields = ['id', 'name', 'description']

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer to represent the Comment model.
    Includes the author's username as a read-only field.
    """
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'author_username', 'created_at']


class PostSerializer(serializers.ModelSerializer):
  author = AuthorSerializer(read_only=True)
  categories = CategorySerializer(many=True, read_only=True)
  class Meta:
    model = Post
    fields = ['id', 'title', 'content', 'author', 'categories', 'publish_date', 'last_modified']

class PostDetailSerializer(serializers.ModelSerializer):
  """
  Detailed serializer for the Post model.
  Includes nested comments, author, and categories serializers.
  """
  author = AuthorSerializer(read_only=True)
  categories = CategorySerializer(many=True, read_only=True)
  comments = CommentSerializer(many=True, read_only=True)
  class Meta:
    model = Post
    fields = ['id', 'title', 'content', 'author', 'categories', 'publish_date', 'last_modified', 'comments']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
      user = User(
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        email=validated_data['email'],
        username=validated_data['username']
      )
      user.set_password(validated_data['password'])
      user.save()
      return user
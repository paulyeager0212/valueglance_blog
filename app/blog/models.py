from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
        return self.name

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
  categories = models.ManyToManyField(Category, related_name='blog_posts')
  publish_date = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title


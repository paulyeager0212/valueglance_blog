from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField(blank=True)

   def __str__(self):
      return self.name

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  publish_date = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  categories = models.ManyToManyField(Category, related_name="posts")

  def __str__(self):
      return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  email = models.EmailField()
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=True)

  class Meta:
     ordering = ['created_on']

  def __str__(self):
     return f'Comment {self.body} by {self.name}'


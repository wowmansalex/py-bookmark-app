from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.tag

class Bookmarks(models.Model):
  user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
  added = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  url = models.URLField(default=None)
  
  class Meta:
    ordering = ['-added']

  def __str__(self):
    return self.title


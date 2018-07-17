from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManayToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

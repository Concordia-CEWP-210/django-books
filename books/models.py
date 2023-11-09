from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    coverImage = models.TextField()
    numPages = models.IntegerField()
    desctipion = models.TextField()
    slug = models.SlugField(unique=True)
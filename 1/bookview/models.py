# Create your models here.
#class Poll(models.Model):
#    question = models.CharField(max_length=200)
#    name = models.CharField(max_length=200)

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    downloadUrl = models.CharField(max_length=1024)
    imageUrl = models.CharField(max_length=1024)


from datetime import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    profilePicture = models.CharField(max_length=100)
    coverPicture = models.CharField(max_length=100)
    followers = models.IntegerField()
    followings = models.IntegerField()

    isAdmin = models.BooleanField()
    description = models.TextField()

    insertedAt = models.CharField(max_length=50)
    updatedAt = models.CharField(max_length=50)

    dateTest = models.DateTimeField(default=None)

    # dateTest1 = models.DateTimeField(auto_now=True)

class Car(models.Model):
    name = models.CharField(max_length=20)
    speed = models.IntegerField()
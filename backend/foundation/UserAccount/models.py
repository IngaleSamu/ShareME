from datetime import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    profilePicture = models.CharField(default=None, max_length=1000, null=True)
    coverPicture = models.CharField(default=None, max_length=1000, null=True)
    followers = models.IntegerField(default=0)
    followings = models.IntegerField(default=0)

    isAdmin = models.BooleanField(default=False)
    description = models.TextField(default=None)

    insertedAt = models.DateTimeField()
    updatedAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    # dateTest = models.DateTimeField(default=None)
    # dateTest1 = models.DateTimeField(auto_now=True)

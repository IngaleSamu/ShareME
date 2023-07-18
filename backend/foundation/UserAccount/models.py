from datetime import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    userId = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    profilePicture = models.CharField(default=None, max_length=1000, null=True)
    coverPicture = models.CharField(default=None, max_length=1000, null=True)
    followers = models.IntegerField(default=0, null=True)
    followings = models.IntegerField(default=0, null=True)

    isAdmin = models.BooleanField(default=False, null=True)
    description = models.TextField(default=None, max_length=1000, null=True)

    insertedAt = models.DateTimeField()
    updatedAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    isPrivate = models.BooleanField(default=True)

class FollowRelationShips(models.Model):
    id = models.AutoField(primary_key=True)
    follower = models.CharField(max_length=50)
    following = models.CharField(max_length=50)
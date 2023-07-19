from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

from foundation.settings import engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(50), nullable=False)
    userId = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)

    description = Column(String(1000))
    profilePicture = Column(String(1000))
    coverPicture = Column(String(1000))
    followers = Column(Integer)
    followings = Column(Integer)
    isActive = Column(Boolean, default=True)
    isPrivate = Column(Boolean, default=True)
    isAdmin = Column(Boolean, default=True)

    createdAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)

class UserFollowList(Base):
    __tablename__ = 'UserFollowList'
    id = Column(Integer, primary_key=True, autoincrement=True)
    follower = Column(String(50), nullable=False)
    following = Column(String(50), nullable=False)

class FollowRequests(Base):
    __tablename__ = 'UserFollowRequest'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(String(50), nullable=False)
    requestedUserId = Column(String(50), nullable=False)
    isAccepted = Column(Boolean, default=False)

# class User(models.Model):
    # id = models.AutoField(primary_key=True)
    # userName = models.CharField(max_length=20)
    # userId = models.CharField(max_length=50)
    # email = models.CharField(max_length=50)
    # password = models.CharField(max_length=128)

    # profilePicture = models.CharField(default=None, max_length=1000, null=True)
    # coverPicture = models.CharField(default=None, max_length=1000, null=True)
    # followers = models.IntegerField(default=0, null=True)
    # followings = models.IntegerField(default=0, null=True)

    # isAdmin = models.BooleanField(default=False, null=True)
    # description = models.TextField(default=None, max_length=1000, null=True)
    #
    # insertedAt = models.DateTimeField()
    # updatedAt = models.DateTimeField(auto_now=True)
    # isActive = models.BooleanField(default=True)
    # isPrivate = models.BooleanField(default=True)

# class UserFollowList(models.Model):
#     id = models.AutoField(primary_key=True)
#     follower = models.CharField(max_length=50)
#     following = models.CharField(max_length=50)
#
# class FollowRequests(models.Model):
#     id = models.AutoField(primary_key=True)
#     userId = models.CharField(max_length=50)
#     requestedUserId = models.CharField(max_length=50)
#     isAccept = models.BooleanField(default=False, null=True)

# Base.metadata.create_all(engine)
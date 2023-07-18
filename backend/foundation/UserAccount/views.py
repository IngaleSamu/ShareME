import uuid
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from Util.Entity.userSearch import SearchParameter
from .models import User, FollowRelationShips
from Util.serializer import model_serializer

def home(request):
    return HttpResponse("Hi, It's the creater !")

# @swagger_auto_schema(
#     method='post',
#     tags=['Users'],
#     request_body=SearchParameter,
#     responses={
#         200: 'Success',
#         400: 'Invalid Request',
#         500: 'Internal Server Error',
#     }
# )
@api_view(['post'])
def get_user(request):
    data = request.data
    # test = SearchParameter
    if data:
        if data.get('name'):
            users = User.objects.filter(userName__contains=data.get('name'))
        elif data.get('userId'):
            users = User.objects.filter(id=data.get('userId'))
        else:
            users = list()
    else:
        users = User.objects.filter(isActive=True)
    serializer = model_serializer(User, querySet=users)
    return Response(serializer)

# @swagger_auto_schema(
#     method='post',
#     tags=['Users'],
#     request_body=model_serializer(User),
#     responses={
#         200: 'Success',
#         400: 'Invalid Request',
#         500: 'Internal Server Error',
#     }
# )
# @api_view(['POST'])
# def add_user(request):
#     request.data['userId'] = str(uuid.uuid4())
#     serializer = model_serializer(User, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

# @swagger_auto_schema(
#     method='post',
#     tags=['Users'],
#     request_body=model_serializer(User),
#     responses={
#         200: 'Success',
#         400: 'Invalid Request',
#         500: 'Internal Server Error',
#     }
# )
@api_view(['POST'])
def update_user(request):
    data = request.data
    try:
        user = User.objects.get(id=data['userId'])
        if 'userName' in data and data['userName']:
            user.userName = data['userName']
        if 'email' in data and data['email']:
            user.email = data['email']
        if 'password' in data and data['password']:
            user.password = data['password']
        if 'profilePicture' in data and data['profilePicture']:
            user.profilePicture = data['profilePicture']
        if 'coverPicture' in data and data['coverPicture']:
            user.coverPicture = data['coverPicture']
        if 'followers' in data and data['followers']:
            user.followers = data['followers']
        if 'followings' in data and data['followings']:
            user.followings = data['followings']
        if 'isAdmin' in data and data['isAdmin']:
            user.isAdmin = data['isAdmin']
        if 'description' in data and data['description']:
            user.description = data['description']
        if 'isActive' in data and data['isActive']:
            user.isActive = data['isActive']
        user.save()
        return Response("Updated user!", status=200)
    except Exception as e:
        return Response("User doesn't exist!", status=400)

# @swagger_auto_schema(
#     method='post',
#     tags=['Users'],
#     request_body=model_serializer(User),
#     responses={
#         200: 'Success',
#         400: 'Invalid Request',
#         500: 'Internal Server Error',
#     }
# )
@api_view(['POST'])
def delete_user(request):
    data = request.data
    try:
        user = User.objects.get(id=data['userId'])
        userName = user.userName
        user.delete()
        return Response(f"Deleted user account of {userName}!", status=200)
    except Exception as e:
        return Response("User doesn't exist!", status=400)

@api_view(['POST'])
def follow_user(request):
    data = request.data
    try:
        userId = data['userId']
        userIdToFollow = data['userIdToFollow']
        user = User.objects.get(userId=data['userIdToFollow'])
        if(user.isPrivate):
            pass
        else:
            userFollow = FollowRelationShips()
            userFollow.follower = userId
            userFollow.following = userIdToFollow
            userFollow.save()
            pass
            return Response(f"Followed user!", status=200)
    except Exception as e:
        return Response(f"Error : {e}", status=400)

@api_view(['POST'])
def perform_follow_request(request):
    data = request.data
    try:
        userId = data['userId']
        appealedUserId = data['userIdToFollow']
        isAccepted = data.get('isAccepted')

        if(isAccepted):
            userFollow = FollowRelationShips()
            userFollow.follower = appealedUserId
            userFollow.following = userId
            userFollow.save()

            user = User.objects.get(userId=data['userId'])
            user.followers += 1
            user.save()

            appealedUser = User.objects.get(userId=data['appealedUserId'])
            appealedUser.followings += 1
            appealedUser.save()

            return Response(f"Followed user!", status=200)
    except Exception as e:
        return Response(f"Error : {e}", status=400)




from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .Entity.userSearch import SearchParameter
from .models import User
from util.serializer import model_serializer

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
@api_view(['POST'])
def add_user(request):
    serializer = model_serializer(User, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

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


import json
import logging
import uuid
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from Util.Entity.userSearch import SearchParameter

from .Service.UserService import UserService # get_user_details, update_user_details, delete_user_account
from .models import User, UserFollowList
from Util.serializer import model_serializer

def home(request):
    return HttpResponse("Hi, It's the creater !")

@api_view(['post'])
def get_user(request):
    data = request.data
    response = {"data": [], "responseMessagae": "OK", "count": 0, "status": 200}
    try:
        fetched_users = UserService(data).get_user_details()
        if(len(fetched_users) > 0):
            response["data"] = json.loads(fetched_users.to_json(orient='records'))
            response["count"] = len(response["data"])
    except Exception as error:
        logging.error("In get_user, Error message is {}".format(error))
        response["responseMessagae"] = "Error in Api"
        response["status"] = 500
    return Response(response)


@api_view(['POST'])
def update_user(request):
    data = request.data
    response = {"data": [], "responseMessagae": "User not updated", "count": 0, "status": 500}
    try:
        updateResult =  UserService(data).update_user_details()
        if (updateResult):
            response["responseMessagae"] = "User updated"
            response["status"] = 200
    except Exception as error:
        logging.error("In update_user, Error message is {}".format(error))
    return Response(response)

@api_view(['POST'])
def delete_user(request):
    data = request.data
    response = {"data": [], "responseMessagae": "User not deleted", "count": 0, "status": 500}
    try:
        deleteResult =  UserService(data).delete_user_account()
        response["responseMessagae"] = deleteResult.get("message")
        response["status"] = 200
    except Exception as error:
        logging.error("In delete_user, Error message is {}".format(error))
    return Response(response)

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
            userFollow = UserFollowList()
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
            userFollow = UserFollowList()
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




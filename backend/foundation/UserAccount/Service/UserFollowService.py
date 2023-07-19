from django.http import HttpResponse
from rest_framework.response import Response

from .models import User, UserFollowList

def home(request):
    return HttpResponse("Hi, It's the creater !")

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




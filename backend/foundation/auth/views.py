import uuid

from django.db.models import Q
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from UserAccount.models import User
from rest_framework.response import Response

from Util.serializer import model_serializer
from Util.encodeDecode import encodePassword


def home(request):
    return HttpResponse("Hi, It's the creater !")


@api_view(['post'])
def register_user(request):
    data = request.data
    try:
        if data and data.get('email') and data.get('passwaord'):
            # availableUser = User.objects.filter(userName=data.get('name') | email=data.get('email'))
            availableUser = User.objects.filter(email=data.get('email'))

            if availableUser:
                return Response("User already registered!", status=200)
            else:
                user = User()
                user.userName = data.get('email')
                if data.get('name'):
                    user.userName = data.get('name')
                user.email = data.get('email')
                user.userId = str(uuid.uuid4())
                user.password = encodePassword(data.get('passwaord'))
                user.insertedAt = datetime.utcnow()
                user.save()
        else:
            return Response("Incomplete data for register!", status=400)
    except Exception as e:
        return Response("Error in register!", status=400)
    return Response('OK')


@api_view(['post'])
def login_user(request):
    data = request.data
    try:
        if data and data.get('email') and data.get('passwaord'):
            password = encodePassword(data.get('passwaord'))
            userExist = User.objects.filter(password=password, email=data.get('email'))
            if (not userExist):
                return Response("User doesn't exist!", status=200)
        else:
            return Response("Invalid data for Login!", status=400)
    except Exception as e:
        return Response("Error in Login!", status=400)
    return Response('OK')
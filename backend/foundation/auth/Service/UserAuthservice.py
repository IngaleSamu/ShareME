import logging
import uuid
from datetime import datetime

from django.http import HttpResponse
from rest_framework.response import Response
from sqlalchemy import func, and_, between
from sqlalchemy.orm import sessionmaker

from foundation.settings import engine
from Util.encodeDecode import encodePassword
from UserAccount.models import User


class UserAuthService:
    def __init__(self, data):
        self.input = data

    def register_user_service(self):
        """method to register users on request"""
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            response = {"responseMessage": "OK", "response": [], "status": 200}
            userExists = session.query(User.userId).filter_by(email=self.input['email']).all()
            if userExists:
                response["response"] = [{"userId": userExists.userId}]
                response['responseMessage'] = 'User Email already exist'
                return response

            password = encodePassword(self.input.get('passwaord'))
            userId = str(uuid.uuid4())
            userName = self.input.get('userName') if (self.input.get('userName')) else self.input.get('email')
            currentDate = datetime.utcnow()
            session.add(User(email=self.input['email'], userId=userId,
                             userName=userName, password=password,
                             createdAt=currentDate, updatedAt=currentDate))
            session.commit()
            session.close()
            response['responseMessage'] = "User registered"
            response["response"] = [{"userId": userId}]
            return response
        except Exception as error:
            session.rollback()
            session.close()
            logging.error("In get_user_details, Error message is {}".format(error))
            return {"responseMessage": "User can't registerd", "response": [], "status": 500}

    def login_user_service(self):
        """method to login users on request"""
        Session = sessionmaker(bind=engine)
        session = Session()
        response = {"responseMessage": "OK", "response": [], "status": 200}
        try:

            if self.input and self.input.get('email') and self.input.get('passwaord'):
                password = encodePassword(self.input.get('passwaord'))
                userExists = session.query(User.email, User.password, User.userId).filter_by(email=self.input['email']).first()
                if userExists:
                    if userExists.password == password:
                        response["response"] = [{"userId": userExists.userId}]
                        response["responseMessage"] = "User login Successfull"
                    else:
                        response["responseMessage"] = "User password is incorrect"
                else:
                    response["responseMessage"] = "User isn't registered for login"
            else:
                response["responseMessage"] = "Invalid data for Login!"
                response["status"] = 400
        except Exception as error:
            session.rollback()
            session.close()
            logging.error("In get_user_details, Error message is {}".format(error))
            response = {"responseMessage": "User Login Failed", "response": [], "status": 500}
        return response


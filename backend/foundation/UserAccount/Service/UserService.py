import logging
from datetime import datetime

import pandas as pd
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker

from foundation.settings import engine
from UserAccount.models import User


# def get_user_details(data):
#     """method to fetch users on request"""
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     userList = []
#     try:
#         filters = []
#         if data.get('name'):
#             search_field = ''.join(('%', data.get('name'), '%'))
#             field1 = 'userName'
#             field2 = 'description'
#             filters.append(or_(getattr(User, field1).like(search_field), getattr(User, field2).like(search_field)))
#         elif data.get('userId'):
#             field = 'userId'
#             filters.append(getattr(User, field) == data.get('userId'))
#
#         filter_object = and_(*filters)
#         rows = session.query(User).filter(filter_object)
#         userList = pd.read_sql_query(rows.statement, rows.session.bind)
#     except Exception as e:
#         logging.error("In get_user_details, Error message is {}".format(e))
#     session.close()
#     return userList
#
#
# def update_user_details(data):
#     """method to update users on request"""
#     result = False
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     try:
#         if data.get("userId"):
#             userId = data.get("userId")
#             userToUpdate = session.query(User).filter(and_(User.userId == userId)).first()
#             if data.get("userName"):
#                 setattr(userToUpdate, 'userName', data.get("userName"))
#             if 'email' in data and data.get("email"):
#                 setattr(userToUpdate, 'email', data.get("email"))
#             if 'password' in data and data.get("password"):
#                 setattr(userToUpdate, 'password', data.get("password"))
#             if 'description' in data and data.get("description"):
#                 setattr(userToUpdate, 'description', data.get("description"))
#             if 'profilePicture' in data and data.get("profilePicture"):
#                 setattr(userToUpdate, 'profilePicture', data.get("profilePicture"))
#             if 'coverPicture' in data and data.get("coverPicture"):
#                 setattr(userToUpdate, 'coverPicture', data.get("coverPicture"))
#             if 'followers' in data and data.get("followers"):
#                 setattr(userToUpdate, 'followers', data.get("followers"))
#             if 'followings' in data and data.get("followings"):
#                 setattr(userToUpdate, 'followings', data.get("followings"))
#             if 'isAdmin' in data and data.get("isAdmin") in [True, False]:
#                 setattr(userToUpdate, 'isAdmin', data.get("isAdmin"))
#             if 'isActive' in data and data.get("isActive") in [True, False]:
#                 setattr(userToUpdate, 'isActive', data.get("isActive"))
#             if 'isPrivate' in data and data.get("isPrivate") in [True, False]:
#                 setattr(userToUpdate, 'isPrivate', data.get("isPrivate"))
#             setattr(userToUpdate, 'updatedAt', datetime.utcnow())
#             session.commit()
#             result = True
#     except Exception as e:
#         logging.error("In update_user_details, Error message is {}".format(e))
#     session.close()
#     return result
#
#
# def delete_user_account(data):
#     """method to fetch users on request"""
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     result = {"message": "", 'isSuccess': False}
#     try:
#         if data.get("userId"):
#             userId = data.get("userId")
#             userToDelete = session.query(User).filter(and_(User.userId == userId)).first()
#             if userToDelete:
#                 session.delete(userToDelete)
#                 session.commit()
#                 result["isSuccess"] = True
#                 result["message"] = "User deleted!"
#             else:
#                 result["message"] = "User doesn't exist!"
#     except Exception as e:
#         session.rollback()
#         logging.error("In get_user_details, Error message is {}".format(e))
#         result["message"] = "Error in User delete!"
#     session.close()
#     return result


class UserService:
    def __init__(self, data):
        self.input = data

    def get_user_details(self):
        """method to fetch users on request"""
        Session = sessionmaker(bind=engine)
        session = Session()
        userList = []
        try:
            filters = []
            if self.input.get('name'):
                search_field = ''.join(('%', self.input.get('name'), '%'))
                field1 = 'userName'
                field2 = 'description'
                filters.append(or_(getattr(User, field1).like(search_field), getattr(User, field2).like(search_field)))
            elif self.input.get('userId'):
                field = 'userId'
                filters.append(getattr(User, field) == self.input.get('userId'))

            filter_object = and_(*filters)
            rows = session.query(User).filter(filter_object)
            userList = pd.read_sql_query(rows.statement, rows.session.bind)
        except Exception as e:
            logging.error("In get_user_details, Error message is {}".format(e))
        session.close()
        return userList

    def update_user_details(self):
        """method to update users on request"""
        result = False
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            if self.input.get("userId"):
                userId = self.input.get("userId")
                userToUpdate = session.query(User).filter(and_(User.userId == userId)).first()
                if self.input.get("userName"):
                    setattr(userToUpdate, 'userName', self.input.get("userName"))
                if 'email' in self.input and self.input.get("email"):
                    setattr(userToUpdate, 'email', self.input.get("email"))
                if 'password' in self.input and self.input.get("password"):
                    setattr(userToUpdate, 'password', self.input.get("password"))
                if 'description' in self.input and self.input.get("description"):
                    setattr(userToUpdate, 'description', self.input.get("description"))
                if 'profilePicture' in self.input and self.input.get("profilePicture"):
                    setattr(userToUpdate, 'profilePicture', self.input.get("profilePicture"))
                if 'coverPicture' in self.input and self.input.get("coverPicture"):
                    setattr(userToUpdate, 'coverPicture', self.input.get("coverPicture"))
                if 'followers' in self.input and self.input.get("followers"):
                    setattr(userToUpdate, 'followers', self.input.get("followers"))
                if 'followings' in self.input and self.input.get("followings"):
                    setattr(userToUpdate, 'followings', self.input.get("followings"))
                if 'isAdmin' in self.input and self.input.get("isAdmin") in [True, False]:
                    setattr(userToUpdate, 'isAdmin', self.input.get("isAdmin"))
                if 'isActive' in self.input and self.input.get("isActive") in [True, False]:
                    setattr(userToUpdate, 'isActive', self.input.get("isActive"))
                if 'isPrivate' in self.input and self.input.get("isPrivate") in [True, False]:
                    setattr(userToUpdate, 'isPrivate', self.input.get("isPrivate"))
                setattr(userToUpdate, 'updatedAt', datetime.utcnow())
                session.commit()
                result = True
        except Exception as e:
            session.rollback()
            logging.error("In update_user_details, Error message is {}".format(e))
        session.close()
        return result

    def delete_user_account(self):
        """method to fetch users on request"""
        Session = sessionmaker(bind=engine)
        session = Session()
        result = {"message": "", 'isSuccess': False}
        try:
            if self.input.get("userId"):
                userId = self.input.get("userId")
                userToDelete = session.query(User).filter(and_(User.userId == userId)).first()
                if userToDelete:
                    session.delete(userToDelete)
                    session.commit()
                    result["isSuccess"] = True
                    result["message"] = "User deleted!"
                else:
                    result["message"] = "User doesn't exist!"
        except Exception as e:
            session.rollback()
            logging.error("In get_user_details, Error message is {}".format(e))
            result["message"] = "Error in User delete!"
        session.close()
        return result

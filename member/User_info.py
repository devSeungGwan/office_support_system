 # -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
########################
# user := (id, email)
#######################

class User_Notice():
    __id = None
    __email = None
    def __init__(self):
       pass

    @staticmethod
    def info_update(_info):   #(id, email)
        User_Notice.__id = _info[0]
        User_Notice.__email = _info[1]

    @staticmethod
    def get_id():
        if User_Notice.__id ==None:
            return False
        else:
            return User_Notice.__id
    @staticmethod
    def get_email():
        if User_Notice.__email == None:
            return False
        else:
            return User_Notice.__email

'''
class User_info():
    user = None
    
    def __init__(self):
        pass

    @classmethod
    def user_init(cls):
        cls.user = None

    @classmethod
    def user_add(cls,info):
        cls.user = info
    
    @classmethod
    def user_id(cls):
        if cls.user == None:
            return False
        else:
            return cls.user[0]

    @classmethod
    def user_email():
        if cls.user == None:
            return False
        else:
            return cls.user[1]
 ''' 

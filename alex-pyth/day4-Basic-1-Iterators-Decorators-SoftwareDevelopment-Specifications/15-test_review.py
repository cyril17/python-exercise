# user,passwd = 'gsy','123'
#
# def auth(auth_type):
#     print('auth_type:',auth_type)
#     def outwarpper(func):
#         def warpper(*args,**kwargs):
#             print('warpper func args:',*args,**kwargs)
#             if auth_type == "local":
#                 username = input('Username:').strip()
#                 password = input('Password:').strip()
#
#                 if user == username and passwd == password:
#                     print('auth pass')
#                     res=func(*args,**kwargs)
#                     return res
#                 else:
#                     print('invalid data')
#             elif auth_type == 'ldap':
#                 print('don\'t know ldap')
#         return warpper
#     return outwarpper
#
# def index.html():
#     print('welcome to index.html')
#
# @auth(auth_type='local')
# def home():
#     print('welcome to home page')
#     return 'from home'
#
# @auth(auth_type='ldap')
# def bbs():
#     print('welcome to bbs page')
#
# index.html()
# home()
# bbs()


import os
import sys


print(__file__)
print(os.path.abspath(__file__))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

print(BASE_DIR)

from conf import settings
from core import main

main.login()



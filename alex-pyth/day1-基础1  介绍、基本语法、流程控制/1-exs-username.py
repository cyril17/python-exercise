# -*- coding:utf-8 -*-
# Author  Cyril

import getpass

_username='gsy'
_password='111'

"""if  _username==usename and _password==password:
    print("you got it!")
else:
"""
d = {}
error = {}
cout = 0
while cout <3:

    username = input("please input username:")
    password = input("input password:")
    if username == error.keys():
        print("you can't login!")
        break
    else:
        if _username==username and _password==password:
            print("you got it",d)
            d[username] = password
            break
        else:
            print("sorry,input error,please input again:")
        cout +=1

error[username] = password
print("you have input error more times,so closed it!")


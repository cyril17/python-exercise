# -*- coding:utf-8 -*-
# Author  Cyril

import getpass

_username='gsy'
_password='111'

"""if  _username==usename and _password==password:
    print("you got it!")
else:
"""
cout = 0
while cout <3:

    usename = input("please input username:")
    password = input("input password:")

    if _username==usename and _password==password:
        print("you got it")
        break
    else:
        print("sorry,input error,please input again:")
    cout +=1
print("you have input error more times,so closed it!")
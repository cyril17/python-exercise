# -*- coding:utf-8 -*-
# Author  Cyril

import getpass

_username='gsy'
_password='111'

username = input("name:")
#password = getpass.getpass("password:")
password = input("password:")

if _username == username and _password == password:
    print("welcome {name} login".format(name=username))
else:
    print("invali username")

  print("hahahah")

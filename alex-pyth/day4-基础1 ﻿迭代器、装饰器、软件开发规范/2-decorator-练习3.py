
##day-4-10

import time

user ,passwd = 'gsy' ,'123'

def auth(auth_type):
    print("auth func:",auth_type)
    def outerwrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)
            if auth_type == "local":
                username = input('please input your name:').strip()
                password = input('please input you passwd').strip()

                if user == username and passwd == password:
                    print('\033[32;1m User has passed authentication\033[0m')
                    res = func(*args, **kwargs)
                    print('-------after authentication-----------')
                    return res
                else:
                    exit('\033[32;1m Invalid username or password\033[0m')
            elif auth_type == "ldap":
                print("不会ldap")
        return wrapper
    return outerwrapper

def index():
    print('welcome to index page')

@auth(auth_type="local")    #相当于home=auth（）
def home():
    print('welcome to home page')
    return 'from home'

@auth(auth_type="ldap")
def bbs():
    print('welcome to bbs page')

index()
print(home())
bbs()

'''
auth func: local
auth func: ldap
welcome to index page
wrapper func args:
please input your name:gsy
please input you passwd123
 User has passed authentication
welcome to home page
-------after authentication-----------
from home
wrapper func args:
不会ldap
'''

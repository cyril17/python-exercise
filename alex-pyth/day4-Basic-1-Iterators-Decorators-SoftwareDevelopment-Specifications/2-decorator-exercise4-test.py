
user,passwd = 'gsy','123'

def auth(auth_type):
    print('auth_type:',auth_type)
    def outwrapper(func):
        def wrapper(*args,**kwargs):
            print('wrapper func args:',*args,**kwargs)
            if auth_type == 'local':
                username = input('Username:').strip()
                password = input('Password:').strip()

                if user == username and passwd == password:
                    print('\033[32;1m Authentication has passed\033[0m')
                    res = func(*args,**kwargs)
                    print('------------after authentication')
                    return res
                else:
                    exit('Invalid username or password')
            elif auth_type == 'ldap':
                print('不会')
        return wrapper
    return outwrapper

def index():
    print('welcome to index.html page')

@auth(auth_type='local')
def home():
    print('welcome to home page')
    return 'from home'

@auth(auth_type='ldap')
def bbs():
    print('welcome to bbs page')

index()
print(home())
bbs()
'''
auth_type: local
auth_type: ldap
welcome to index.html page
wrapper func args:
Username:gsy
Password:123
 Authentication has passed
welcome to home page
------------after authentication
from home
wrapper func args:
不会
'''
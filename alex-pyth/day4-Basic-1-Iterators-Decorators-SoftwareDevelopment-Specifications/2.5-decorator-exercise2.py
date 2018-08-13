user,passwd = 'gsy','123'

def auth(func):
    def wrapper(*args,**kwargs):
        username = input('please input your name:').strip()
        password = input('please input you passwd').strip()

        if user == username and passwd == password:
            print('\033[32;1m User has passed authentication\033[0m')
            func(*args,**kwargs)
        else:
            exit('\033[32;1m Invalid username or password\033[0m')
    return wrapper

def index():
    print('welcome to index.html page')

@auth
def home():
    print('welcome to home page')

@auth
def bbs():
    print('welcome to bbs page')

index()
home()
bbs()

'''
welcome to index.html page
please input your name:gsy
please input you passwd123
 User has passed authentication
welcome to home page
please input your name:fd
please input you passwd21
 Invalid username or password
'''
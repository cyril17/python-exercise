
user,passwd = 'gsy','123'

def auth(func):
    def wrapper(*args,**kwargs):
        username = input('Username:').strip()
        password = input('Password:').strip()

        if user == username and passwd == password:
            print('\033[32;1m Authentication has passed\033[0m')
            func(*args,**kwargs)
        else:
            exit('Invalid username or password')
    return wrapper

def index():
    print('welcome to index page')

@auth
def home():
    print('welcome to home page')

@auth
def bbs():
    print('welcome to bbs page')

index()
home()
bbs()
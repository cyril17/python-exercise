user,passwd = 'gsy','123'

def auth(func):
    def warpper(*args,**kwargs):
        Username = input('Username:')
        Password = input('Password:')

        if user == Username and passwd == Password:
            print('auth pass')
            #func(*args,**kwargs)
        else:
            print('invalid data')
    return warpper


def index():
    print('welcome to index')

@auth
def home():
    print('welcome to home page')

@auth
def bbs():
    print('welcome to bbs page')

index()
home()
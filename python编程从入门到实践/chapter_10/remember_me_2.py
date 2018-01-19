import json

filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what is your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("we will remember you!" + username + "!")
else:
    print("Welcome back " + username + "!")

'''
将用户的信息存储，并判断用户是否已经存储消息
10.4.2
'''
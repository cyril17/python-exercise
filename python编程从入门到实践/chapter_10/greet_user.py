import json

filename = 'username.json'

with open(filename) as file_obj:
    username = json.load(file_obj)

print("Welcome to back " + username + "!")

'''
读取用户存储的信息
运行结果
Welcome to back gsy!
'''
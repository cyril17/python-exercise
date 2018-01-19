import json

username = input("What is your name? ")

filename = 'username.json'

with open(filename,'w') as file_object:
    json.dump(username,file_object)
    print("We will back,when you come back.")

'''
会将用户输入的信息"gsy"  写入username.json保存
运行结果
What is your name? gsy
We will back,when you come back.

'''
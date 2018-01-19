import json

filename = 'numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)

'''
使用json.load将存储的数据读取到内存中
运行结果
[2, 3, 5, 7, 11, 13]
'''


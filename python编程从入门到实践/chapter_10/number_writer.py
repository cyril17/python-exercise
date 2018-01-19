import json

numbers = [2,3,5,7,11,13]

filname = 'numbers.json'

with open(filname,'w') as file_object:
    json.dump(numbers,file_object)

'''
运行结果
在numbers.json中将会存储[2, 3, 5, 7, 11, 13]
'''
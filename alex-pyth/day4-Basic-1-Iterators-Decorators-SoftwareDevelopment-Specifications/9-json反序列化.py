#
# import json
#
# f  = open("test.txt","r")
# data = json.loads(f.read())
#
# print(data['age'])
#
# f.close()
# #22
#
# #序列化就是把内存的数据对象变成字符串，存到了硬盘上面，



import pickle    #pickle只能在Python中使用

def sayhi(name):
    print('helo2',name)     #即使内容不一样，只要函数名一样。就可以反序列化

f  = open("test.txt","rb")
data = pickle.loads(f.read())

print(data['func']('GSY'))

f.close()
'''
helo2 GSY
None
'''



#序列化就是把内存的数据对象变成字符串，存到了硬盘上面，
# f  = open("test.txt","r")
# data = eval(f.read())
# print(data['age'])
# f.close()
# '''
# 22
# '''

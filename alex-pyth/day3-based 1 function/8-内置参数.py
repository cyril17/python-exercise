


# print(all([1,-5,3]))
# print(all([0,-1,3]))
# print(any([0,-1,3]))
# '''
# True
# False
# True
# '''
#
# a = ascii([1,2,'哈哈'])
# print(a)
# #[1, 2, '\u54c8\u54c8']
# print(type(a))
# #<class 'str'>
#
# #把一个数字转换为二进制
# print(bin(255))
# #0b11111111

# #bytearray
# a = bytes('abcde',encoding='utf-8')
# b = bytearray('defg',encoding='utf-8')
# print(a.capitalize(),a)
# #b'Abcde' b'abcde'    # 不可改变
# print(a[0])
# #97   打印出来的是ASCII码
# print(b)
# b[1] = 100
# print(b)
# '''
# bytearray(b'defg')
# bytearray(b'ddfg')
# '''

# def sayhi():pass
# print(callable(sayhi))
# print(callable([]))
# True
# False

# print(chr(98))
# #b   将ascii码转换为字符
#
# print(ord('b'))
# #98   将字符转换为ASCII码
#


# print(divmod(5,2))
# print(divmod(5,3))
# print(divmod(5,5))
# '''
# (2, 1)
# (1, 2)
# (1, 0)
# 返回商和余数
# '''


#匿名函数
# def sayhi(n):
#     print(n)
#
# sayhi(3)
#
# print(lambda n:print(n))
# calc = lambda n:print(n)
# calc(5)
# '''
# 3
# <function <lambda> at 0x1009f7a60>
# 5
# '''

# res = filter(lambda n:n>5,range(10))
# for i in res:
#     print(i)
# '''
# 6
# 7
# 8
# 9
# fillter就是根据前面的函数，根据要求过滤出相应的数据
# '''

# res = map(lambda n:n*n,range(10))
# res = [lambda n:n*n,for n in range(10)  上下同样效果
# for i in res:
#     print(i)
# '''
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
#就是根据前面的函数，根据要求过滤出相应的数据
# '''

# #reduce
# import functools
#
# res = functools.reduce(lambda x,y:x+y,range(10))
# print(res)
# #45    从0开始加到10，累加   ，x是结果，y是值，
#

# print(hex(43))
# #0x2b     把一个数字转换成16进制
#

# def test.yaml():
#     lcoal_var = 333
#     print(locals())
#
# test.yaml()
# print(globals())
# print(globals().get('local_var'))
# '''
# {'lcoal_var': 333}
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x107cb95c0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/cyril/Documents/python-exercise/python-exercise/alex-pyth/day3-based 1 function/8-内置参数.py', '__cached__': None, 'test.yaml': <function test.yaml at 0x107e0c840>}
# None
# '''

# print(pow(2,3))
# #8     2的3次方

#round(1.5678)

# a = {6:2,8:0,1:4,-5:6,99:README.md,4:22}
# print(a)
# print(sorted(a))
# print(sorted(a.items(),key=lambda x:x[1]))   #以value排序
# print(sorted(a.items()))                     #以key排序
# '''
# {6: 2, 8: 0, 1: 4, -5: 6, 99: README.md, 4: 22}
# [-5, 1, 4, 6, 8, 99]
# [(8, 0), (6, 2), (1, 4), (-5, 6), (99, README.md), (4, 22)]
# [(-5, 6), (1, 4), (4, 22), (6, 2), (8, 0), (99, README.md)]
# '''


# a = [1,2,3,4]
# b = ['a','b','c','d']
#
# for i in zip(a,b):
#     print(i)
# '''
# (1, 'a')
# (2, 'b')
# (3, 'c')
# (4, 'd')
# 将2个列表一一对应
# '''



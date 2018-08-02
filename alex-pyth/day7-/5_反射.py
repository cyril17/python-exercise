# -*- coding: utf-8 -*-
'''
反射：
    实现了一个董涛的内存装配
    hasattr(obj,name_str)   判断一个对象obj里面是否含有name_str字符串的方法
    getattr(obj,name_str)   根据字符串name_str，去获取obj里对应方法的内存地址
    setattr(obj,'y',z)      想当于， obj.y = z
    delattr(obj,name_str)
'''

def bulk(self):
    print('%s is bulk,,,,,,' % self.name)

class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s' % (self.name, food))

d = Dog('gsy')
# d.eat('txy')

choice = input('>>>:').strip()
if hasattr(d, choice):
    # delattr(d,choice)
    func = getattr(d, choice)  # 获取内存对象地址，如果是静态地址的话就会直接返回值，如果是方法的话会直接去调用
    func('666')
else:
    # setattr(d,choice,None)   #指定默认为空
    # v = getattr(d,choice)
    # print(v(bulk()))
    setattr(d, choice, bulk)
    func = getattr(d, choice)
    func(d)

print(d.name)
'''
gsy
'''

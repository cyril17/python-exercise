# -*- coding: utf-8 -*-
'''
类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量
'''

class Dog(object):
    name = '666'

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        print('%s is eating' %(self.name))

    def talk(self, obj):
        print('%s is talking with %s' % (self.name, obj))

d = Dog('哈哈哈')
d.eat()
d.talk('txy')

'''
666 is eating
哈哈哈 is talking with txy

'''

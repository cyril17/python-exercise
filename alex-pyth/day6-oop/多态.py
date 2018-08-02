# -*- coding: utf-8 -*-


class Animal(object):
    def __init__(self,name):
        self.name = name

    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print('miao miao miao')

class Cat(Animal):
    def talk(self):
        print('woof woof woof')

def func(obj):
    obj.talk()   #一种接口多种实现，将c1或者d1作为obj传入


# d1 = Dog('test1')
# c1 = Cat('test2')
# d1.talk()
# c1.talk()

d1 = Dog('test1')
c1 = Cat('test2')

func(d1)
func(c1)
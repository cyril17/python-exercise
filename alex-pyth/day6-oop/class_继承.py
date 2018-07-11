# -*- coding: utf-8 -*-

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eating ' %self.name)

    def talk(self):
        print('shuo hua ')

    def sleep(self):
        print('%s is sleeping ' %self.name)

class Man(People):

    def piao(self):   #在父类的基础上新加属性
        print('%s is piao'%self.name)

    def talk(self):   #重构父类之后再次调用talk的话显示的是子类中的talk,如果希望父类中定义的生效，再次引用父类，People.talk(self)
        People.talk(self)
        print('i am no')

class Woman(People):

    def get_birth(self):
        print('so birth')

m1 = Man('gsy',20)
m1.piao()
m1.talk()

w1 = Woman('txy',20)
w1.get_birth()
w1.sleep()
#w1.piao()    子类之间是不能相互直接调用的
'''
gsy is piao
shuo hua 
i am no
so birth
txy is sleeping 
'''


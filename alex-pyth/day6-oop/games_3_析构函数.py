# -*- coding: utf-8 -*-

class Role:
    n = 123   #在这里定义的就叫做类变量
    name = 'hahahah '
    n_list = []
    def __init__(self,name,role,weapon,life_value=100):
        #名称叫构造函数
        #作用是为了实例化类的时候传参数，做一些类的初始化的工作

        self.name = name       #r1.name=name 实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value

    def __del__(self):     #不用传参数给他，析构函数
        print('%s 彻底死了，，，'%self.name )

    def shot(self):         #类的方法，功能（动态属性）
        print('shooting')

    def get_shot(self):
        print('ah,,,,,I got shot')

    def buy_gun(self,gun_name):
        print('%s just bought %s ' %(self.name,gun_name))


r1 = Role('gsy1','police','m3')     #把一个类变成一个具体对象的过程叫实例化（初始化一个类，造了一个对象）
r1.buy_gun('ak489')
r1.get_shot()

del r1

r2 = Role('gsy2','prove','tes')     #把一个类变成一个具体对象的过程叫实例化（初始化一个类，造了一个对象）
r2.buy_gun('666')
r2.get_shot()

'''
不加del r1
gsy1 just bought ak489 
ah,,,,,I got shot
gsy2 just bought 666 
ah,,,,,I got shot
gsy1 彻底死了，，，
gsy2 彻底死了，，，

加del r1  ，r1实例会立即结束，所以马上会执行析构函数
gsy1 just bought ak489 
ah,,,,,I got shot
gsy1 彻底死了，，，
gsy2 just bought 666 
ah,,,,,I got shot
gsy2 彻底死了，，，

'''




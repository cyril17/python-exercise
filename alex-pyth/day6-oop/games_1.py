# -*- coding: utf-8 -*-


class Role:
    n = 123   #在这里定义的就叫做类变量
    def __init__(self,name,role,weapon,life_value=100):
        #名称叫构造函数
        #作用是为了实例化类的时候传参数，做一些类的初始化的工作

        self.name = name       #实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value

    def shot(self):        #类的方法，功能（动态属性）
        print('shooting')

    def get_shot(self):
        print('ah,,,,,I got shot')

    def buy_gun(self,weapon):
        print('%s just bought %s ' %(self.name,self.weapon))

r1 = Role('gsy1','police','m3')     #把一个类变成一个具体对象的过程叫实例化（初始化一个类，造了一个对象）
#相当于
#

r2 = Role('gsy2','x3','ak47')       #生成一个角色
r3 = Role('gsy3','tou','ju')

r1.shot()
r2.get_shot()
r3.buy_gun('ju')
'''
shooting
ah,,,,,I got shot
gsy3 just bought ju 
'''
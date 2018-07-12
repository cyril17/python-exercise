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
        self.__life_value = life_value   #私有属性就是在这个变量前面加2横杠

    def show_status(self):      #把私有属性写在另一个函数里面
        self.__life_value -=50
        print('name:%s weapon:%s life_val:%s' %(self.name,self.weapon,self.__life_value))

    def __shot(self):        #私有方法
        print('shooting')

    def get_shot(self):
        print('ah,,,,,I got shot')

    def buy_gun(self,gun_name):
        print('%s just bought %s ' %(self.name,gun_name))


r1 = Role('gsy1','police','m3')     #把一个类变成一个具体对象的过程叫实例化（初始化一个类，造了一个对象）
r1.buy_gun('m4')

r1.get_shot()
print(r1.show_status())
#r1.__shot()  私有方法在外部也不能调用

'''
gsy1 just bought m4 
ah,,,,,I got shot
name:gsy1 weapon:m3 life_val:50
None
'''




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

    def shot(self):        #类的方法，功能（动态属性）
        print('shooting')

    def get_shot(self):
        print('ah,,,,,I got shot')

    def buy_gun(self,weapon):
        print('%s just bought %s ' %(self.name,self.weapon))

print(Role.n)   #在没有实例化的时候就可以直接打印值

r1 = Role('gsy1','police','m3')     #把一个类变成一个具体对象的过程叫实例化（初始化一个类，造了一个对象）
r1.name = 'gsy666'
r1.bullet_prove = True       #给类中加一个
print(r1.weapon)
r1.n_list.append('from r1 list')
r1.n = '66666'       #这里看是改类变量，但这个相当于在R1里面写了一条R1='666666'，所以此变量的赋值在R1中生效，找的时候还是从本地开始找
print('r1:',r1.weapon,r1.n,Role.n,r1.n_list)   #
# del r1.weapon    #删了之后在实例中就没有了，会报错，会提示AttributeError: 'Role' object has no attribute 'weapon'

print(r1.weapon)
print(r1.n,r1.name,r1.bullet_prove)

r2 = Role('gsy2','x3','ak47')       #生成一个角色
r2.n_list.append('from r2 list')
r2.name = 'gsy888'
print('r2:',r2.name,r2.n)     #如果实例 中没有name这个实例变量先去类变量中找，如果实例中有，则先调用实例中的

Role.n = '改类变量'

print(r1.n,r2.n,Role.n,r2.n_list)

print('ROle.n_list:',Role.n_list)  #说明n_list里面包含了r1 r2中增加的内容

'''
123
m3
r1: m3 66666 123 ['from r1 list']
m3
66666 gsy666 True
r2: gsy888 123
66666 改类变量 改类变量 ['from r1 list', 'from r2 list']
ROle.n_list: ['from r1 list', 'from r2 list']
'''





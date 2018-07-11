# -*- coding: utf-8 -*-

#class People:  经典类
class People(object):    #新式类，与经典类不同的是多继承的继承方式
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eating ' %self.name)

    def talk(self):
        print('shuo hua ')

    def sleep(self):
        print('%s is sleeping ' %self.name)

class Relation(object):

    def make_friends(self,obj):    #先去执行Man里面的name的赋值操作，然后才去父类找
        print('%s is tring making friends with %s' %(self.name,obj.name))

class Man(People,Relation):
                                            #对函数进行重构
    def __init__(self,name,age,money):     #如果要在初始化的时候在父类的基础上再多传入参数，
        #People.__init__(self,name,age)     #再次申明父类的几个参数
        super(Man,self).__init__(name,age)  #比上一行更高级的写法，是新式类的写法
        self.money = money
        print('%s 一出生就有 %s money'%(self.name,self.money))

    def piao(self):   #在父类的基础上新加属性
        print('%s is piaoing '%self.name)

    def talk(self):   #重构父类之后再次调用talk的话显示的是子类中的talk,如果希望父类中定义的生效，再次引用父类，People.talk(self)
        People.talk(self)
        print('i am no')

class Woman(People,Relation):

    def get_birth(self):
        print('so birth')

m1 = Man('gsy',20,10)
m1.piao()
m1.talk()

w1 = Woman('txy',20)
w1.get_birth()
w1.sleep()
#w1.piao()    子类之间是不能相互直接调用的
m1.make_friends(w1)


'''
gsy is piao
shuo hua 
i am no
so birth
txy is sleeping 
'''


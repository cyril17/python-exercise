# -*- coding: utf-8 -*-
'''
属性方法
'''

class Dog(object):
    name = '666'

    def __init__(self, name):
        self.name = name
        self.__food = None

    @property  # 属性方法，将一个方法变成一个静态属性
    def eat(self):
        print('%s is eating %s' % (self.name, self.__food))

    @eat.setter  # 如果需要传入参数，才用这个 ，就相当于修改了
    def eat(self, food):
        print('set for food:', food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print('删除完毕!')

    def talk(self, obj):
        print('%s is talking with %s' % (self.name, obj))


d = Dog('哈哈哈')
d.eat
'''
他已经是一个属性了，在调用的时候不用再加括号了，不能再直接传入参数
如果需要加参数则使用这个
    @eat.setter
    def eat(self,food):
        print('set for food:',food)
        self.__food = food
如果需要加参数后将这个存下来，则
        self.__food = None
        print('%s is eating %s' %(self.name,self.__food))
        self.__food = food

'''

print('--------')
d.eat = 'baozi'
d.eat
del d.eat
# d.eat    # 删完之后再次调用会报错   AttributeError: 'Dog' object has no attribute '_Dog__food'

'''
哈哈哈 is eating None
--------
set for food: baozi
哈哈哈 is eating baozi
删除完毕!
'''

# -*- coding: utf-8 -*-

'''
静态方法名义上归类管理，但是实际上在静态方法里面访问不了类或者实例中的任何属性
'''

class Dog(object):

    def __init__(self, name):
        self.name = name

    @staticmethod  # 把eat变成静态方法了，但静态方法实际就是和类没有关系，不需要传入参数
    def eat():
        print('%s is eating %s' % ('gsy', 'food'))

    def talk(self, obj):
        print('%s is talking with %s' % (self.name, obj))


d = Dog('哈哈哈')
d.eat()  # 静态方法实际就是和类没有关系了，不需要传入参数
d.talk('txy')
Dog.eat()

'''
   如果非要传入参数，则用下面，自己糊弄自己
 @staticmethod   #静态方法实际就是和类没有关系了，不需要传入参数
    def eat(self):
        print('%s is eating %s'%(self.name,'food'))
 d.eat(d)  #静态方法实际就是和类没有关系了，不需要传入参数
 就相当于一个工具包，import  os  ,os.system
'''

'''
gsy is eating food
哈哈哈 is talking with txy
gsy is eating food

'''
# -*- coding: utf-8 -*-

class foo(object):
    '''此类是解释__doc__的作用'''
    def obj(self):
        print('hahaha ')


print(foo.__doc__)
'''
#此类是解释__doc__的作用

'''


class Too:
    '''﻿注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；
        而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()'''
    def __init__(self):
        pass

    def __call__(self,*args,**kwargs):
        print('calling',args,kwargs)


obj = Too()  # 执行 __init__
obj()  # 执行 __call__
obj(1,2,3,name=333)
Too()(1,2,3,name=666)   #2中方法一样的效果

'''
calling () {}
calling (1, 2, 3) {'name': 333}
calling (1, 2, 3) {'name': 666}
'''




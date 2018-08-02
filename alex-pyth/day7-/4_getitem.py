# -*- coding: utf-8 -*-

class Foo(object):
    '''﻿用于索引操作，如字典。以上分别表示获取、设置、删除数据'''

    def __init__(self):
        self.data = {}   #这相当于把实例变成一个字典了

    def __getitem__(self, key):
        print('__getitem__', key)
        return self.data.get(key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.data[key] = value  #这相当于把实例变成一个字典了

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

#result = obj['k1']  # 自动触发执行 __getitem__
obj['k2'] = 'gsy'  # 对实例赋值，自动触发执行 __setitem__
#__setitem__ k2 gsy
print(obj.data)  #这相当于把实例变成一个字典了，打印的话就会打印值
#{'k2': 'gsy'}
print(obj['k2'])
#gsy

#del obj['k2']    #
#__delitem__   k2

# -*- coding: utf-8 -*-

class GsyException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return '哈哈'      #如果执行下面的self.message 就会打印'我的异常'
    '''
    def __str__(self):
        return self.message
    '''

try:
    raise GsyException('我的异常')    #raise就是触发自己写的异常
except GsyException as e:
    print(e)

'''
哈哈
'''
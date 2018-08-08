# -*- coding: utf-8 -*-
#自动IO切换
import gevent

def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m')
    gevent.sleep(2)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')

def func3():
    print('running func3 ')
    gevent.sleep(0)    #0秒只是触发切换的操作
    print('running func3 again')


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3),
])

'''
李闯在跟海涛搞...
李闯切换到了跟海龙搞...
running func3 
running func3 again
李闯搞完了海涛，回来继续跟海龙搞...
李闯又回去跟继续跟海涛搞...
'''
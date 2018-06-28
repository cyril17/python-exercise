#
#
#
# def bar():
#     print('in the bar')
#
#
# def foo():
#     print('in the foo')
#     bar()
#
# foo()

# def foo():
#     print('in the foo')
#     bar()
#
# def bar():
#     print('in the bar')
#
#
# foo()


'''
import time

def bar():
    time.sleep(3)
    print('in the bar')

def test1(func):
    start_time = time.time()
    func()    #run bar
    stop_time = time.time()
    print('the func run time is %s' %(stop_time-start_time))

test1(bar)


# in the bar
# the func run time is 3.002976894378662

'''

import time

def bar():
    time.sleep(3)
    print('in the bar')

def test2(func):
    print(func)
    return func

#print(test2(bar))

#t=test2(bar)
#print(t)
"""
<function bar at 0x10a72ff28>
<function bar at 0x10a72ff28>
"""
# t=test2(bar)
# t()
"""
<function bar at 0x10a72ff28>
in the bar
"""

bar=test2(bar)   #把之前定义的bar覆盖了
bar()
"""
<function bar at 0x10a72ff28>
in the bar
"""

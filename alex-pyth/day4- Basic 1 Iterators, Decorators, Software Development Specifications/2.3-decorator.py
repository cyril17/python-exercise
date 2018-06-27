

import time

#装饰器
def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return

#调用装饰器的时候用@就可以，不会影响原函数的运行
@timmer
def test1():
    time.sleep(3)
    print('in the test1')

test1()
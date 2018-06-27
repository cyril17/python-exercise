




# import time
#
# def deco(func):
#
#     start_time=time.time()
#     func()
#     stop_time=time.time()
#     print('the func run time is %s ' %(stop_time-start_time))
#
# def test1():
#     time.sleep(3)
#     print('in thwe test1')
#
# def test2():
#     time.sleep(3)
#     print('in the test2')
#
# deco(test1)
# deco(test2)
#
# '''
# in thwe test1
# the func run time is 3.005173921585083
# in the test2
# the func run time is 3.000221014022827
# '''







# import time
#
# def deco(func):
#
#     start_time=time.time()
#     return func
#     stop_time=time.time()
#     print('the func run time is %s ' %(stop_time-start_time))
#
# def test1():
#     time.sleep(3)
#     print('in thwe test1')
#
# def test2():
#     time.sleep(3)
#     print('in the test2')
#
# test1=deco(test1)
# test1()
#
# test=deco(test2)
# test2()
#
# '''
# in thwe test1
# in the test2
# '''

import time

def timer(func):   #func=test1   ，这里有函数的嵌套
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)        #run  test1
        stop_time=time.time()
        print('the func run time is %s ' %(stop_time-start_time))
    return deco     #not  deco()   ，这里引用了高阶函数

@timer  #test1=timer(test1)  #只timeer(test1)返回的是韩式的额内存地址，加括号才是运行结果
def test1():
    time.sleep(3)
    print('in thwe test1')

@timer   #test2 = timer(test2) = deco    test2()=deco()
def test2(name,age):
    time.sleep(3)
    print('in the test2',name,age)

#开始调用
test1()
test2('gsy',20)   #当他运行到func()的时候，没有传入参数，故出错
#实现了装饰器的功能，既没有改变函数的内容，也没有改变他的调用方式

'''
in thwe test1
the func run time is 3.004528760910034 
in the test2 gsy 20
the func run time is 3.000276803970337 
'''

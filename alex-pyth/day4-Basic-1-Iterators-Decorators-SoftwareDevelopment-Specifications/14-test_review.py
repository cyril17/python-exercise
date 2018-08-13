# # # # # # #
# # # # # # # a = [1,2,3,4,5,6,7,8,9,10]
# # # # # # # b=[]
# # # # # # #
# # # # # # # for i in a:
# # # # # # #     b.append(i+1)
# # # # # # #
# # # # # # # a = b
# # # # # # # print(a)
# # # # # # #
# # # # # # # print('------------------------------------')
# # # # # # #
# # # # # # # for index.html,i in enumerate(a):
# # # # # # #     a[index.html] +=1
# # # # # # #
# # # # # # # print(a)
# # # # # # # print('------------------------------------')
# # # # # # #
# # # # # # # a = map(lambda x:x+1,a)
# # # # # # # b=[]
# # # # # # # for i in a:
# # # # # # #     b.append(i)
# # # # # # # print(b)
# # # # # # # print('------------------------------------')
# # # # # # #
# # # # # # # #a = [1,2,3,4,5,6,7,8,9,10]
# # # # # # # #print(a)
# # # # # # # a = （i+1 for i in range(1,11))
# # # # # # # print(a)
# # # # # # #
# # # # # #
# # # # # #
# # # # # # # def fib(max):
# # # # # # #     n, a, b = 0, 0, 1
# # # # # # #     while n < max:
# # # # # # #         yield b
# # # # # # #         a,b = b,a+b
# # # # # # #         n = n+1
# # # # # # #     return 'done'
# # # # # # #
# # # # # # # data = fib(10)
# # # # # # #
# # # # # # # print(data.__next__())
# # # # # # # print(data.__next__())
# # # # # # # print(data.__next__())
# # # # # # # print(data.__next__())
# # # # # # # print(data.__next__())
# # # # # # #
# # # # # # #
# # # # # # # for i in data:
# # # # # # #     print(i)
# # # # # # #
# # # # # # #
# # # # # # # print(data)
# # # # # #
# # # # # # def fib(max):
# # # # # #     n, a, b = 0, 0, 1
# # # # # #     while n < max:
# # # # # #         yield b
# # # # # #         a,b = b,a+b
# # # # # #         n = n+1
# # # # # #     #return 'done'
# # # # # #
# # # # # # data = fib(10)
# # # # # #
# # # # # #
# # # # # # while True:
# # # # # #     try:
# # # # # #         ff = next(data)
# # # # # #         print('ff',ff)
# # # # # #     except StopIteration as e:
# # # # # #         print('666',e.value)
# # # # # #         break
# # # # #
# # # # #
# # # # # import time
# # # # # def consumer(name):
# # # # #     print("%s 准备吃包子啦!" %name)
# # # # #     while True:
# # # # #        baozi = yield
# # # # #
# # # # #        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
# # # # #
# # # # #
# # # # # def producer(name):
# # # # #     c = consumer('A')
# # # # #     c2 = consumer('B')
# # # # #
# # # # #     print("老子开始准备做包子啦!")
# # # # #     c.__next__()
# # # # #     c2.__next__()
# # # # #     for i in range(10):
# # # # #         time.sleep(1)
# # # # #         print("做了2个包子!")
# # # # #         c.send(i)
# # # # #         c2.send(i)
# # # # #
# # # # # producer("gsy")
# # # # #
# # # #
# # # # import time
# # # #
# # # # def timmer(func):
# # # #     def warpper(*args,**kwargs):
# # # #         start_time = time.time()
# # # #         func()
# # # #         stop_time = time.time()
# # # #         print('the func run time is %s' %(stop_time-start_time))
# # # #     return
# # # #
# # # # @timmer
# # # # def test1():
# # # #     time.sleep(3)
# # # #     print('in the test1')
# # # #
# # # #
# # # # test1()
# # # #
# # # #
# # # #
# # # #
# # # #
# # #
# # import time
# #
# # def bar():
# #     time.sleep(2)
# #     print('int the bar')
# #
# # def test1(func):
# #     start_time = time.time()
# #     func()
# #     stop_time = time.time()
# #     print('the fun run time is %s ' %(stop_time-start_time))
# #     return func
# #
# # # test1(bar)
# # # print('------')
# # # t=test1(bar)
# # # print('----------',t)
# # # print('666')
# # # t()
# # print('-------')
# # bar = test1(bar)
# # print('-------')
# # bar()
#
#
#
# def foo():
#     print('in the foo')
#     def bar():
#         print('in the bar')
#     bar()
#
# foo()

import time

def timmer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print('run time %s' %(stop_time-start_time))
    return deco

@timmer
def test1():
    time.sleep(3)
    print('in the test1')

@timmer
def test2(name,age):
    time.sleep(3)
    print('in the test2',name,age)

test1()
test2('gsy',22)
















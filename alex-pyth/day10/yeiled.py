# -*- coding: utf-8 -*-
import time
import queue


def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield     #第一次会停在这，函数里面有yield，第一次加括号会变成生成器，第一次并没有真正执行
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(1)

def producer():
    r = con.__next__()    #第一次会变成一个生成器，
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()

'''
--->starting eating baozi...
--->starting eating baozi...
[c1] is eating baozi 1
[c2] is eating baozi 1
[producer] is making baozi 1
[c1] is eating baozi 2
[c2] is eating baozi 2
[producer] is making baozi 2
[c1] is eating baozi 3
[c2] is eating baozi 3
[producer] is making baozi 3
[c1] is eating baozi 4
[c2] is eating baozi 4
[producer] is making baozi 4
[c1] is eating baozi 5
[c2] is eating baozi 5
[producer] is making baozi 5
'''
# -*- coding: utf-8 -*-

from multiprocessing import Process, Manager


def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(1)
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()   #生成一个字典，可以在多个进程之间共享和传递

        l = manager.list(range(5))  #生成一个列表，可以在多个进程之间共享和传递
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)


'''
[0, 1, 2, 3, 4, 1]
[0, 1, 2, 3, 4, 1, 1, 1]
[0, 1, 2, 3, 4, 1, 1, 1]
[0, 1, 2, 3, 4, 1, 1, 1, 1, 1]
[0, 1, 2, 3, 4, 1, 1, 1, 1, 1]
[0, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1]
[0, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
{1: '1', '2': 2, 0.25: None}
[0, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
'''
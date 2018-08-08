# -*- coding: utf-8 -*-

import multiprocessing
import time,threading

def thread_run():
    print(threading.get_ident())

def run(name):
    time.sleep(2)
    print('hello',name)
    q = threading.Thread(target=thread_run,)  #进程里面套线程
    q.start()


if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run,args=('bob %s!'%i,))
        p.start()
p.join()

# -*- coding: utf-8 -*-

from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.send([42, None, 'hello2'])
    print('from paret:',conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    print(parent_conn.recv())  # prints "[42, None, 'hello2']"
    parent_conn.send('你好，子进程')
    p.join()

'''
[42, None, 'hello']
[42, None, 'hello2']
from paret: 你好，子进程
'''



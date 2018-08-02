# -*- coding: utf-8 -*-


class A:
    def __init__(self):
        print('A')

class B(A):
    pass
    # def __init__(self):
    #     print('B')

class C(A):
    def __init__(self):
        print('C')

class D(B,C):
    pass
    # def __init__(self):
    #     print('')

obj = D()

#C
'''
﻿如果有构造函数，先找d-b-c-a,这叫广度优先，先横向再纵向往上   


在python2上面 经典类 是按照深度查询去操作的
             新式类是按照广度查询去操作的
             
在python3上面 经典类 是按照广度查询去操作的
             新式类是按照深度查询去操作的
'''
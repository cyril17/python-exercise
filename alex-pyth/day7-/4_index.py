# -*- coding: utf-8 -*-

from lib.aa import C

obj = C()
print(obj.__module__)   #﻿# 输出 lib.aa，即：输出模块
print(obj.__class__)     ﻿# 输出 lib.aa.C，即：输出类

'''
lib.aa
<class 'lib.aa.C'>
'''


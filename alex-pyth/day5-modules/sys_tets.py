# -*- coding: utf-8 -*-

import sys

print(sys.version)
# 3.6.5 (default, Apr 25 2018, 14:23:58)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)]

# ﻿返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.path)
# ['/Users/cyril/Documents/python-exercise/python-exercise/alex-pyth/day5-modules', '/Users/cyril/Documents/python-exercise/python-exercise', '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages', '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend']

#
print(sys.platform)
# darwin    返回操作系统平台名称

print(sys.stdout.write('please'))
# please6

print(sys.stdout.write('pleasewqwq'))
# pleasewqwq10

val = sys.stdin.readline()[:-1]
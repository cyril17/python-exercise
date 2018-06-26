
import time

def logger():
    time_format = '%Y-%m-%d %X'    #x代表小时分钟秒
    time_current = time.strftime(time_format)
    with open('14-a.txt','a+') as f:
        f.write(' %s logger add success!\n' %time_current)

def func1():
    print("in the func1")
    logger()

#过程，过程返回值为空
def func2():
    print("in the func2")
    logger()
    return 0

def func3():
    print("in the func3")
    logger()
    return 1,[1,2,3,4],{"ewe":"ewew","s":"ewt"}

func1()
func2()
func3()

print(func1())
print(func2())
print(func3())

'''
在14-a.txt中会增加如下
 2018-06-21 22:50:33 logger add success!
 2018-06-21 22:50:33 logger add success!
 2018-06-21 22:50:33 logger add success!
 
'''

'''
in the func1
in the func2
in the func3

in the func1
None
in the func2
0
in the func3
(1, [1, 2, 3, 4], {'ewe': 'ewew', 's': 'ewt'})
'''

'''
﻿总结：

        返回值数=0；返回None，﻿结束函数运行

        返回值数=1；返回object

        返回值数>1；返回tuple
'''
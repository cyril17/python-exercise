# -*- coding: utf-8 -*-

import random

print(random.random())
#0.0850521768239294
#产生 0 到 1 之间的随机浮点数

print(random.randint(1,4))
#随机生成1到4的随机整数
print(random.randrange(1,10))
#随机生成1到9的整数
print(random.uniform(1.3,6.5))
#产生1.3到6.5的随机浮点数
print(random.choice('tomorrow'))
#随机产生字符串中的单个字符

print(random.randrange(1,100,2))
## 生成从1到100的间隔为2的随机整数(全是奇数)

a = [1,2,3,4,5,6]
random.shuffle(a)
print(a)
'''
[2, 6, 3, 4, 5, 1]
将序列a中的元素顺序打乱
'''

生成随机验证码

checkcode = ''
for i in range(4):
    current = random.randrange(0,4)   #顾头不顾尾，只循环0到3
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)

print(checkcode)


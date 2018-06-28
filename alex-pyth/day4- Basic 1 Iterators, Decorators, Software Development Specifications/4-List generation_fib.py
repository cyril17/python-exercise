
#斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b   #返回当前运行的值
        a, b = b, a + b
        n = n + 1
    return '此处的错误'
#这个return会返回异常


data = fib(10)
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())   #此行为11行，多余，则报错

print('-------------')
for i in data:
    print(i)


'''
Traceback (most recent call last):
1
1
  File "/Users/cyril/Documents/python-exercise/python-exercise/alex-pyth/day4- Basic 1 Iterators, Decorators, Software Development Specifications/4-List generation_fib.py", line 26, in <module>
2
    print(data.__next__())
3
5
StopIteration: 此处的错误
8
13
21
34
55

'''





'''
1      a=0,b=1
2      a=1,b=1,
3      a=1,b=2
4      a=2,b=3
5      a=3,b=5
6      a=5,b=8
7      a=8,b=13
8      a=13,b=21
9      a=21,b=34
10     a=34,b=55
11
'''

#斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(10)

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
README.md
'''
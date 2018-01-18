#print(5/0)

'''
运行结果
Traceback (most recent call last):
  File "D:/python-exercise/python编程从入门到实践/chapter_10/division.py", line 1, in <module>
    print(5/0)
ZeroDivisionError: division by zero
'''
#为了避免将错误消息展现给用户，使用try-expect,10.3.2

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

'''
运行结果
You can't divide by zero!
'''
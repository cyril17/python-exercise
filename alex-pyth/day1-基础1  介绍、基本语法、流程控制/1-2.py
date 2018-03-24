# -*- coding:utf-8 -*-
# Author  Cyril

name = input("name:")
age = int(input("age:"))

salary = input("salary:")

info = '''
 ------------info  %s   --------
 
 Name:%s
 Age:%d
 Salary:%s
''' % (name,name,age,salary)

print(info)
print(type(age),type(str(age)))

"""
name:gsy
age:32
salary:32

 ------------info  gsy   --------
 
 Name:gsy
 Age:32
 Salary:32

<class 'int'> <class 'str'>
"""
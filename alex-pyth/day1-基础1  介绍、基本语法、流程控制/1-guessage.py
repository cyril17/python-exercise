# -*- coding:utf-8 -*-
# Author  Cyril

my_age = 26

age = int(input("guess age:"))

if  age == my_age:
    print("you got it")
elif age > my_age:
    print("more better")
else:
    print("small better")
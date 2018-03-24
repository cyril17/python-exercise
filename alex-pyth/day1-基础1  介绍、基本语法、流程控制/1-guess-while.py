# -*- coding:utf-8 -*-
# Author  Cyril

my_age = 26

cout = 0
while cout < 3:
    age = int(input("guess age:"))
    if  age == my_age:
        print("you got it")
        break
    elif age > my_age:
        print("more better")
    else:
        print("small better")
    cout += 1
else:
#if cout == 3:
    print("fuck off")


import os

import sys

print(__file__)   #在哪个目录下运行此文件，就返回当前目录的相对路径,

print(os.path.abspath(__file__))   #返回当前文件的绝对路径

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )   #返回当前项目的父目录的绝对路径


sys.path.append(BASE_DIR)   #将项目目录所在的路径加入环境变量，需要导入sys模块

print(BASE_DIR)
from conf import settings
from core import main

main.login()




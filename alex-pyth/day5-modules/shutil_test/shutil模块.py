# -*- coding: utf-8 -*-

import shutil

f1 = open('qw1',encoding='utf-8')

f2 = open('qw2','w',encoding='utf-8')

shutil.copyfileobj(f1,f2)

#将qw1的内容拷贝到qw2中去


shutil.copyfile('qw1','qw3')
和上面的功能一样，将qw1的内容拷贝一份到qw3


#将a目录以gztar的格式压缩到当前目录下的目录下，以a_test为名字
shutil.make_archive('./c/a_test','gztar','/Users/cyril/Documents/python-exercise/python-exercise/alex-pyth/day5-modules/shutil_test/a')


# -*- coding: utf-8 -*-

import shutil

f1 = open('qw1',encoding='utf-8')

f2 = open('qw2','w',encoding='utf-8')

shutil.copyfileobj(f1,f2)

#将qw1的内容拷贝到qw2中去



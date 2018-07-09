# -*- coding: utf-8 -*-

class dog:

    def __init__(self,name):
        self.name = name

    def bulk(self):
        print('%s: wang wang wang' %self.name)

d1 = dog('狗1')
d2 = dog('狗2')
d3 = dog('狗3')

d1.bulk()
d2.bulk()
d3.bulk()

'''
狗1: wang wang wang
狗2: wang wang wang
狗3: wang wang wang
'''

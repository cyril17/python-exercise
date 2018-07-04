# -*- coding: utf-8 -*-


import time

print(time.time())  #显示当时的时间戳
#1530632813.114658
#print(time.sleep(3))

#返回Fri Aug 19 12:38:29 2016 格式, 同上
print(time.asctime())
#Tue Jul  3 23:46:56 2018
print(time.asctime(time.localtime()))
#Wed Jul  4 07:33:49 2018
print(time.ctime())
#Tue Jul  3 23:46:56 2018

#时间戳转换为结构化时间即struct_time
print(time.localtime())        #
#time.struct_time(tm_year=2018, tm_mon=7, tm_mday=3, tm_hour=23, tm_min=58, tm_sec=16, tm_wday=1, tm_yday=184, tm_isdst=0)
print(time.localtime(1530633805.521607))
#time.struct_time(tm_year=2018, tm_mon=7, tm_mday=4, tm_hour=0, tm_min=3, tm_sec=25, tm_wday=2, tm_yday=185, tm_isdst=0)
print(time.gmtime())
#time.struct_time(tm_year=2018, tm_mon=7, tm_mday=3, tm_hour=16, tm_min=14, tm_sec=52, tm_wday=1, tm_yday=184, tm_isdst=0)
print(time.gmtime(1530633805.521607))
#time.struct_time(tm_year=2018, tm_mon=7, tm_mday=3, tm_hour=16, tm_min=3, tm_sec=25, tm_wday=1, tm_yday=184, tm_isdst=0)

#将结构化语言转换为时间戳
print(time.mktime(time.localtime()))
#1530634210.0
print(time.mktime(time.gmtime()))
#1530605874.0

#将结构化语言转换为格式化字符串时间
print(time.strftime("%Y-%m-%d %X",time.localtime()))
#2018-07-03 23:59:26
print(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()))
#2018-07-04 07-43-44
#将格式化的时间戳改为结构化系统
print(time.strptime('2018-07-03 13:33:33','%Y-%m-%d %X'))
#time.struct_time(tm_year=2018, tm_mon=7, tm_mday=3, tm_hour=13, tm_min=33, tm_sec=33, tm_wday=1, tm_yday=184, tm_isdst=-1)



print('---------------------')

import datetime

#将时间戳转换为格式化时间
print(datetime.datetime.now())
#2018-07-04 00:43:02.177600
print(datetime.date.fromtimestamp(1530607382.0))
#2018-07-03
print(datetime.datetime.now())
#2018-07-04 00:43:02.177600

#将当前时间增加或者减少3天
print(datetime.datetime.now()+datetime.timedelta(+3))
#2018-07-07 00:45:21.352559
print(datetime.datetime.now()+datetime.timedelta(-3))
#2018-07-01 00:46:24.520186

#将当前时间增加或者减少3小时
print(datetime.timedelta(hours=3))
#3:00:00
print(datetime.timedelta(hours=-3))
#-1 day, 21:00:00
print(datetime.timedelta(minutes=3))
#0:03:00



# -*- coding: utf-8 -*-

import pymysql

#创建连接
conn = pymysql.connect(host='localhost',port=3306,user='cyril',password='123456',db='testdb')

#创建游标
cursor = conn.cursor()

# 执行SQL，并返回受影响行数
effect_row = cursor.execute('select * from student')
print(effect_row)  #返回4
print(cursor.fetchone())   #取一条数据
print(cursor.fetchone())   #取一条数据
print('--------')
print(cursor.fetchall())   #取出全部数据

'''
4
(1, 'txy', 22, datetime.date(2018, 8, 8), None)
(3, 'gsy', 20, datetime.date(2018, 5, 8), None)
--------
((5, 'cyril', 21, datetime.date(2010, 5, 8), None), (9, 'ghl', 30, datetime.date(2010, 5, 8), None))
'''

#提交，不然无法保存新建或者修改数据
conn.commit()

#关闭游标
cursor.close()

#关闭连接
conn.close()
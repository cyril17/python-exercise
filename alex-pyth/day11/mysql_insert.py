# -*- coding: utf-8 -*-

import pymysql

#创建连接
conn = pymysql.connect(host='localhost',port=3306,user='cyril',password='123456',db='testdb')

#创建游标
cursor = conn.cursor()

data = [
    ('N1',12,'2019-01-01','play football'),
    ('N2',12,'1990-01-01','play basketball'),
    ('N3',12,'2020-01-01','play tennis'),
]

cursor.executemany('insert into student (name,age,register_date,hob) values(%s,%s,%s,%s)',data)


#提交，不然无法保存新建或者修改数据,因为它自动开启了事务，
conn.commit()

#关闭游标
cursor.close()

#关闭连接
conn.close()

'''
mysql>  select * from student;
+----+-------+-----+---------------+-----------------+
| id | name  | age | register_date | hob             |
+----+-------+-----+---------------+-----------------+
|  1 | txy   |  22 | 2018-08-08    | NULL            |
|  3 | gsy   |  20 | 2018-05-08    | NULL            |
|  5 | cyril |  21 | 2010-05-08    | NULL            |
|  9 | ghl   |  30 | 2010-05-08    | NULL            |
| 10 | N1    |  12 | 2019-01-01    | play football   |
| README.md | N2    |  12 | 1990-01-01    | play basketball |
| 12 | N3    |  12 | 2020-01-01    | play tennis     |
+----+-------+-----+---------------+-----------------+
7 rows in set (0.00 sec)

mysql> 

'''
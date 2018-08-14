# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

#创建一个连接
engine = create_engine("mysql+pymysql://root:123456@localhost/testdb",
                       encoding='utf-8')  #echo的作用就是打印所有的东西

Base = declarative_base()  # 生成orm基类

class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s>" %(self.id,self.name)


Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例, # coursor

# user_obj = User(name="gsy", password="123456")  # 生成你要创建的数据对象
# user_obj2 = User(name="txy", password="1314")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj2)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建

# data = Session.query(User).filter_by(name='gsy').all()
##如果filter_by里面不加查的具体对象，则过滤出来的是所有对象的内存地址

# print(data)   #打印这个对象的地址
# print(data[0].name,data[0].password)  #因为已经是一个列表，所有
# '''
# [<__main__.User object at 0x1094b9668>, <__main__.User object at 0x1094b97b8>]
# gsy 123456
# '''

data = Session.query(User).filter_by().all()
#如果filter_by里面不加查的具体对象，则过滤出来的是所有对象的内存地址，
#如果要显示所有的具体的值，则在上面创建表字段的时候写repr
print(data)
#[<1 name:gsy>, <2 name:gsy>, <3 name:txy>, <4 name:gl>]

#查询id大于2的
data = Session.query(User).filter(User.id>2).all()
print(data)
#[<3 name:txy>, <4 name:gl>]


data = Session.query(User).filter(User.id==2).all()
print('---',data)
#[<2 name:gsy>]

data = Session.query(User).filter_by(id=2).all()
print(data)
#[<2 name:gsy>]

#多条件查询
data = Session.query(User).filter(User.id>1).filter(User.id<3).all()
print('多条件查询',data)
#多条件查询 [<2 name:gsy>]



#修改
data = Session.query(User).filter(User.id>1).filter(User.id<3).first()
print('修改',data)
data.name = "GSY"
data.password = "Helloworld"
print('修改后',data)
# 修改 <2 name:GSY>
# 修改后 <2 name:GSY>



#回滚
my_user = Session.query(User).filter_by(id=1).first()
my_user.name = "Jack"
fake_user = User(name='Rain', password='12345')
Session.add(fake_user)

print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有你刚添加和修改的数据

Session.rollback()  # 此时你rollback一下

print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 再查就发现刚才添加的数据没有了。


#统计
print(Session.query(User).filter(User.name.in_(['gsy'])).count())  # 再查就发现刚才添加的数据没有了。
#2
'''
这里不区分大小写
mysql> select * from user;
+----+------+------------+
| id | name | password   |
+----+------+------------+
|  1 | gsy  | 123456     |
|  2 | GSY  | Helloworld |
|  3 | txy  | 1314       |
|  4 | gl   | 123456     |
|  6 | ghx  | 1212       |
+----+------+------------+
5 rows in set (0.00 sec)
'''

#分组
print(Session.query(func.count(User.name),User.name).group_by(User.name).all())
#[(1, 'ghx'), (1, 'gl'), (2, 'gsy'), (1, 'txy')]


Session.commit()  # 现此才统一提交，创建数据

'''
[<1 name:gsy>, <2 name:gsy>, <3 name:txy>, <4 name:gl>]
'''


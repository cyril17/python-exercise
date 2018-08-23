# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

#创建一个连接
engine = create_engine("mysql+pymysql://root:123456@localhost/testdb",
                       encoding='utf-8', echo=True)  #echo的作用就是打印所有的东西

Base = declarative_base()  # 生成orm基类

class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例, # coursor

user_obj = User(name="gsy", password="123456")  # 生成你要创建的数据对象
user_obj2 = User(name="txy", password="1314")  # 生成你要创建的数据对象
print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
Session.add(user_obj2)  # 把要创建的数据对象添加到这个session里， 一会统一创建
print(user_obj.name, user_obj.id)  # 此时也依然还没创建

Session.commit()  # 现此才统一提交，创建数据

'''
2018-08-09 16:27:16,372 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
2018-08-09 16:27:16,372 INFO sqlalchemy.engine.base.Engine {}
2018-08-09 16:27:16,374 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
2018-08-09 16:27:16,374 INFO sqlalchemy.engine.base.Engine {}
2018-08-09 16:27:16,374 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
2018-08-09 16:27:16,374 INFO sqlalchemy.engine.base.Engine {}
2018-08-09 16:27:16,375 INFO sqlalchemy.engine.base.Engine SELECT CAST('test.yaml plain returns' AS CHAR(60)) AS anon_1
2018-08-09 16:27:16,375 INFO sqlalchemy.engine.base.Engine {}
2018-08-09 16:27:16,376 INFO sqlalchemy.engine.base.Engine SELECT CAST('test.yaml unicode returns' AS CHAR(60)) AS anon_1
2018-08-09 16:27:16,376 INFO sqlalchemy.engine.base.Engine {}
2018-08-09 16:27:16,376 INFO sqlalchemy.engine.base.Engine SELECT CAST('test.yaml collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
2018-08-09 16:27:16,376 INFO sqlalchemy.engine.base.Engine {}
2018-08-09 16:27:16,377 INFO sqlalchemy.engine.base.Engine DESCRIBE `user`
2018-08-09 16:27:16,377 INFO sqlalchemy.engine.base.Engine {}
gsy None
gsy None
2018-08-09 16:27:16,380 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2018-08-09 16:27:16,380 INFO sqlalchemy.engine.base.Engine INSERT INTO user (name, password) VALUES (%(name)s, %(password)s)
2018-08-09 16:27:16,380 INFO sqlalchemy.engine.base.Engine {'name': 'gsy', 'password': '123456'}
2018-08-09 16:27:16,381 INFO sqlalchemy.engine.base.Engine INSERT INTO user (name, password) VALUES (%(name)s, %(password)s)
2018-08-09 16:27:16,381 INFO sqlalchemy.engine.base.Engine {'name': 'txy', 'password': '1314'}
2018-08-09 16:27:16,382 INFO sqlalchemy.engine.base.Engine COMMIT
'''
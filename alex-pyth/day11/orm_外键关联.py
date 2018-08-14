# -*- coding: utf-8 -*-

import time
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

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    register_date = Column(String(32),nullable=False)
    hob = Column(String(32),nullable=False)

    def __repr__(self):
        return "<%s name:%s>" %(self.id,self.name)


Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例, # coursor


#连表查询
print(Session.query(User,Student).filter(User.id==Student.id).all())


Session.commit()  # 现此才统一提交，创建数据

'''
[<1 name:gsy>, <2 name:gsy>, <3 name:txy>, <4 name:gl>]
'''







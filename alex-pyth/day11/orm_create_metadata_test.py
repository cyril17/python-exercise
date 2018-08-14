# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

#创建一个连接
engine = create_engine('mysql+pymysql://root:123456@localhost/testdb',
                       encoding='utf-8',echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()

user_obj = User(name='gl',password='123456')

Session.add(user_obj)

Session.commit()
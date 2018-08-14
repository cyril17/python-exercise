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


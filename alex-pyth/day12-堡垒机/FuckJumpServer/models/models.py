# -*- coding: utf-8 -*-
#存放表结构

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, Enum, ForeignKey,UniqueConstraint, Table, MetaData
from . import db, login_manager
from sqlalchemy.orm import relationship

from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import ChoiceType,PasswordType

Base = declarative_base()  # 生成orm基类

host_m2m_remoteuser = Table('host_m2m_remoteuser', Base.metadata,
             Column('host_id', Integer, ForeignKey('host.id')),
             Column('remoteuser_id', Integer,ForeignKey('remote_user.id')),
             )
#建立多对多的关联，host到remote_user


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),unique=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)
    remote_users = relationship('RemoteUser',secondary=host_m2m_remoteuser,backref='hosts')

    def __repr__(self):
        return self.hostname

class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True)
    def __repr__(self):
        return self.name

class RemoteUser(Base):
    __tablename__ = 'remote_user'
    id = Column(Integer,primary_key=True)
    username = Column(String(32))
    password = Column(String(128 ),unique=True)
    AuthTypes = [
        ('ssh-password', 'SSH/Password'),
        ('ssh-key', 'SSH/KEY'),
    ]    #第一个存到数据库，第二个显示给用户看
    auth_type = Column(ChoiceType(AuthTypes))
    __table_args__ = (UniqueConstraint('auth_type', 'username','password', name='_user_passwd_uc'),)
    #数据库里面这3个联合唯一，_user_passwd_uc为数据库里面的联合唯一键，就相当于把这三个键放一起做哈希存放
    def __repr__(self):
        return self.username

class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer,primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(128))
    def __repr__(self):
        return self.username



class AuditLog(Base):
    __tablename__ = 'auditlog'
    id = Column(Integer,primary_key=True)
    date = Column(DATE,unique=True)
    username = Column(UserProfile.username,)
    cmd = Column(String(64))
    def __repr__(self):
        return self.username

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例, # coursor




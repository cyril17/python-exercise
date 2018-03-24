# -*- coding:utf-8 -*-
# Author  Cyril

name = input("name:")
age = input("age:")
job = input("job:")
info = '''

----- info {_name} -----
Name: {_name}
Age: {_age}
Job: {_job}
''' .format(_name=name,
            _age=age,
            _job=job)

print(info)

"""
name:gsy
age:32
job:32


----- info gsy -----
Name: gsy
Age: 32
Job: 32
"""
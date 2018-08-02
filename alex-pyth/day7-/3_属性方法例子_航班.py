# -*- coding: utf-8 -*-
#属性方法的应用

class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        print("checking flight %s status " % self.flight_name)
        return 1

    @property       #将方法变为属性，
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print("flight got canceled...")
        elif status == 1:
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter      #加入setter之后就可以传入参数，即修改参数
    def flight_status(self,status):
        print('flight %s changed %s ' %(self.flight_name,status))


f = Flight("CA980")
f.flight_status
f.flight_status = 2

'''
checking flight CA980 status 
flight is arrived...
flight CA980 changed 2 
'''
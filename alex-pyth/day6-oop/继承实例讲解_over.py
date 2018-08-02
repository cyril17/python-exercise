# -*- coding: utf-8 -*-
class SchoolMember(object):
    members = 0   #初始学校位人

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def tell(self):
        pass
    def enroll(self):
        '''注册'''
        SchoolMember.members +=1
        print('\033[32;1m joined members %s ,now is %s members\033[0m' %(self.name,SchoolMember.members))

    def __del__(self):
        '''析构方法'''
        print('\033[32;1m members %s is dead \033[0m')

class Teacher(SchoolMember):

    def __init__(self,name,age,course,salary):
        super(Teacher,self).__init__(name,age)
        self.course = course
        self.salary = salary
        self.enroll()     #教师这里调用了注册

    def teaching(self):
        print('%s teaching %s '%(self.name,self.course))
    def tell(self):
        msg = '''my name is %s ,work for school and course is %s''' %(self.name,self.course)
        print(msg)

class Students(SchoolMember):
    def __init__(self,name,age,grade,sid):
        super(Students,self).__init__(name,age)
        self.grade = grade
        self.sid = sid
    def tell(self):
        print('i am a student,my grade is %s' %(self.grade))

if __name__=='__main__':

    t1 = Teacher('Gsy',20,'python',1000)
    t2 = Teacher('Txy',10,'python',2000)

    s1 = Students('gsy',12,'第十',12323)
    s2 = Students('txy',22,'第2',4567)

    t1.teaching()
    t2.teaching()
    s1.tell()
'''
 joined members Gsy ,now is 1 members
 joined members Txy ,now is 2 members
Gsy teaching python 
Txy teaching python 
i am a student,my grade is 第十
 members %s is dead 
 members %s is dead 
 members %s is dead 
 members %s is dead 
'''

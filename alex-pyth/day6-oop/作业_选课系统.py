# -*- coding: utf-8 -*-

class School(object):
    def __init__(self,name,address,city,course):
        self.name = name
        self.address = address
        self.city = city
        self.course = []
        self.students = []

class Course(School):
    def __init__(self,name,address,city,course,price,outline):
        super(Course,self).__init__(name,address,city,course)
        self.price = price
        self.outline = outline
    def course_type(self,course_name):
        print('you will choose the course %s' %course_name.name)


class Class_num(School,Course):
    def __init__(self,name,address,city,course,price,outline):
        super(Class_num,self).__init__(name,address,city,course,price,outline)

class Student(object):


class Teacher(Class_num):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
        ---- info of Teacher:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course [%s]" %(self.name,self.course))






school_1 = School('dongguan','beij','linux')
school_2 = School('erxiao','hanghai','python')





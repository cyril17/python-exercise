class Car():
    '''一次模拟汽车的简单测试9.2.1'''

    def __init__(self,make,model,year):
        '''初始化描述汽车信息'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriprive_name(self):
        '''得到整洁的描述信息'''
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi','a6',2016)
print(my_new_car.get_descriprive_name() )
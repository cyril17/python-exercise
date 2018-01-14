class Car():
    '''一次模拟汽车的简单测试,给属性修改默认值'''

    def __init__(self,make,model,year):
        '''初始化描述汽车信息'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriprive_name(self):
        '''得到整洁的描述信息'''
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车里程数的消息'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi','a6',2016)
print(my_new_car.get_descriprive_name() )
my_new_car.read_odometer()

'''
运行结果
2016 Audi A6
This car has 0 miles on it.
'''
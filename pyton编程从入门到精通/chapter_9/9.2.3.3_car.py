class Car():
    '''一次模拟汽车的简单测试,通过方法对属性的值增加'''

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
    def update_odometer(self,mileage):
        '''将里程表的数值设置为制定的数值'''
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increament_odometer(self,miles):
        '''将里程数增加到指定的量'''
        self.odometer_reading += miles


my_new_car = Car('audi','a6',2016)
print(my_new_car.get_descriprive_name() )

my_new_car.update_odometer(60)
my_new_car.read_odometer()

my_new_car.increament_odometer(100)
my_new_car.read_odometer()
'''
运行结果
2016 Audi A6
This car has 60 miles on it.
This car has 160 miles on it.
'''
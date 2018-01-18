class Car():
    '''一次模拟汽车的简单测试,继承,将实例用作属性'''

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increament_odometer(self,miles):
        '''将里程数增加到指定的量'''
        self.odometer_reading += miles


class Battery():
    '''模拟电动汽车电瓶的简单测试'''
    def __init__(self,battery=70):
        '''初始化电瓶的属性'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''打印一条描述电瓶容量的信息'''
        print("This car has " + str(self.battery_size) + "-kwh battery.")


class ElectricCar(Car):
    '''电动汽车的独到之处'''

    def __init__(self,make,model,year):
        '''初始化父类的信息'''
        super().__init__(make,model,year)
        self.battery = Battery()


my_tesla  = ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriprive_name())
my_tesla.battery.describe_battery()
'''
运行结果
2016 Tesla Model S
'''
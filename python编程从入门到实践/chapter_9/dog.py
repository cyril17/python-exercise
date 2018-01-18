class Dog():
    '''模拟小狗的简单测试9.1.1'''

    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟被下命令时小狗蹲下'''
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        '''模拟小狗被下命令时打滚'''
        print(self.name.title() + " rolled over.")

my_dog = Dog('xiaobai',6)
print(my_dog.name.title() + "!" + str(my_dog.age) )

from dog import Dog
'''导入dog.py中的Dog类'''

my_dog = Dog('xiaobai',6)
print(my_dog.name.title() + "!" + str(my_dog.age) )
my_dog.sit()
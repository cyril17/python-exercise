
def change_name():
    print("before names:",names)
    names[0] = 'GSY'
    print("change name:",names)

names = ['gsy','txy','gt']

change_name()

print(names)
'''
before names: ['gsy', 'txy', 'gt']
change name: ['GSY', 'txy', 'gt']
['GSY', 'txy', 'gt']
'''

#字符串，单独整数在函数中是不能修改全局变量的，但是列表，集合，字典，类是可以在函数中修改全局变量的
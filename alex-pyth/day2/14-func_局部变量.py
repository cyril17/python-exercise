
def change_name(name):
    # 如果想要在函数里面让局部变量生效，则需要在函数中声明要修改的这个变量
    global school    #在函数里面把school变为全局变量，这种方法不好，不要用！！！！
    school = 'dajing'
    print("before name:",name)
    name = "GSY"     #这个函数就是这个变量的作用域，这个变量只在这个函数中生效
    print("change name:",name)

name = 'gsy'
school = 'tianshui'

change_name(name)

print(name)
print('change-school',school)
'''
before name: gsy
change name: GSY
gsy
change-school dajing
'''

#虽然已经变成大写


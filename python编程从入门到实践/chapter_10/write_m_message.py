filename = 'programming.txt'
'''write()函数不会在末尾加换行符，需要自己加'''
with open(filename,'w') as file_object:
    file_object.write("dsdsdsdsd\n")
    file_object.write("33333333\n")

'''

不加换行符运行结果
dsdsdsdsd33333333
加换行符
dsdsdsdsd
33333333
'''
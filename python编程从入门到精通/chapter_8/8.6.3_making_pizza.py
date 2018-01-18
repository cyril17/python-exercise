#导入函数的时候使用函数的别名（如果函数名跟现有的函数名冲突可这样做）
from pizza import make_pizza as mmp

mmp(16,'popperoni')
mmp(12,'mushrooms','green peppers','extra cheese')

'''
运行结果
Making 16's pizza with following topping:
- popperoni

Making 12's pizza with following topping:
- mushrooms
- green peppers
- extra cheese
'''
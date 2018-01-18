##导入模块的时候使用模块的别名（如果模块名过长或者其他）
import pizza as nnd

nnd.make_pizza(16,'popperoni')
nnd.make_pizza(12,'mushrooms','green peppers','extra cheese')

'''
运行结果
Making 16's pizza with following topping:
- popperoni

Making 12's pizza with following topping:
- mushrooms
- green peppers
- extra cheese
'''
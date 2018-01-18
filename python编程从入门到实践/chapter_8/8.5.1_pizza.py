#结合使用位置实参和任意数量的实参，如果要让函数接受不同类型的实参，必须在函数的定义中将接纳任意数量的实参的形参放在最后
def make_pizza(size,*toppings):
    print("\nMaking's " + str(size) + "'s pizza with following topping:")

    for topping in toppings:
        print("- "+ topping)

make_pizza(16,'11')
make_pizza(12,'11','22','33')

'''
运行结果
Making's 16's pizza with following topping:
- 11

Making's 12's pizza with following topping:
- 11
- 22
- 33

'''
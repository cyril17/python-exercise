#传递任意数量的实参
'''
def make_pizza(*toppings):
    print(toppings)

make_pizza('peppweoni')
make_pizza('11','22','33')

"""
运行结果
('peppweoni',)
('11', '22', '33')
"""
'''

def make_pizza(*toppings):
    print("\nMaking a pizza with the following topping:")
    for topping in toppings:
        print('- '+ topping)
make_pizza('11')
make_pizza('11','22','33')

'''
运行结果
Making a pizza with the following topping:
- 11

Making a pizza with the following topping:
- 11
- 22
- 33

'''
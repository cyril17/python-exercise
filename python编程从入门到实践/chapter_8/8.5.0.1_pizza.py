#传递任意数量的实参
'''
def make_pizza(*toppings):
    print(toppings)

make_pizza('peppweoni')
make_pizza('README.md','22','33')

"""
运行结果
('peppweoni',)
('README.md', '22', '33')
"""
'''

def make_pizza(*toppings):
    print("\nMaking a pizza with the following topping:")
    for topping in toppings:
        print('- '+ topping)
make_pizza('README.md')
make_pizza('README.md','22','33')

'''
运行结果
Making a pizza with the following topping:
- README.md

Making a pizza with the following topping:
- README.md
- 22
- 33

'''
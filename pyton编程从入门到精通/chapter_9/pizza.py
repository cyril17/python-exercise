#此处为8.6.1练习
def make_pizza(size,*toppings):
    print("\nMaking " + str(size) + "'s pizza with following topping:")
    for topping in toppings:
        print("- " + topping)
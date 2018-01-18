unprinted_designs = ['iphone','robot','card','shoe']
compeleted_modules = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("printing design: " + current_design)
    compeleted_modules.append(current_design)

print("\nThe following modules have been printed:")
for compeleted_module in compeleted_modules:
    print(compeleted_module)
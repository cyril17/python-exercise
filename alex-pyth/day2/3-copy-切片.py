import copy

person = ['name',['sex',100],'number']

p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)

print(p1)
print(p2)
print(p3)
print(person.index('number'))

'''
['name', ['sex', 100]]
['name', ['sex', 100]]
['name', ['sex', 100]]
'''
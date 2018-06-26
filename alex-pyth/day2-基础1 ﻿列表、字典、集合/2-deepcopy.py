import copy

names = ["gsy","txy","tt","bb",["al","ph"]]

names4 = copy.deepcopy(names)
print('deepcopy-----',names)
print('deepcopy-----',names4)

names[1] = "666"
names[4][0] = "go"
print(names)
"""
deepcopy----- ['gsy', 'txy', 'tt', 'bb', ['al', 'ph']]
deepcopy----- ['gsy', 'txy', 'tt', 'bb', ['al', 'ph']]
['gsy', '666', 'tt', 'bb', ['go', 'ph']]
"""
#列表的循环
for i  in names:
    print(i)
'''
gsy
666
tt
bb
['go', 'ph']
'''
print(names)
print(names[::2])
'''
names = ['gsy','txy','tdb','wq','re','re','tt']

print(names[0],names[2])
print(names[0::3])

names.append('我是no')
print(names)

names.insert(1,'bb')
print(names)

names[3] = 'go'
print(names)

del names[3]
print(names)

names.remove('tt')
print(names)

names.pop()
print('pop-----',names)

names2 = [1,2,3]
names.extend(names2)
print('extend-----',names)

#names.clear()
#print(names)
'''

'''
names = ["gsy","txy","tt","bb",["al","ph"]]
names3 = names.copy()
print(names)
print(names3)
names[1] = "666"
names[4][0] = "go"
print(names)
print(names3)
'''
#浅copy
['gsy', 'txy', 'tt', 'bb', ['al', 'ph']]
['gsy', 'txy', 'tt', 'bb', ['al', 'ph']]
['gsy', '666', 'tt', 'bb', ['go', 'ph']]
['gsy', 'txy', 'tt', 'bb', ['go', 'ph']]
'''
'''

'''
names = ["gsy","txy","tt","bb",["al","ph"]]
names3 = copy.copy(names)
print(names)
print(names3)
names[1] = "666"
names[4][0] = "go"
print(names)
print(names3)
'''
#浅copy,无论改names还是names3，都会变
['gsy', 'txy', 'tt', 'bb', ['al', 'ph']]
['gsy', 'txy', 'tt', 'bb', ['al', 'ph']]
['gsy', '666', 'tt', 'bb', ['go', 'ph']]
['gsy', 'txy', 'tt', 'bb', ['go', 'ph']]
'''
'''
import copy

names = ["gsy","txy","tt","bb",["al","ph"]]

names[1] = "666"
names[4][0] = "go"
print(names)
print(names3)
'''
浅copy,无论改names还是names3，都会变
['gsy', 'txy', 'tt', 'bb', ['al', 'ph']]
['gsy', 'txy', 'tt', 'bb', ['al', 'ph']]
['gsy', '666', 'tt', 'bb', ['go', 'ph']]
['gsy', 'txy', 'tt', 'bb', ['go', 'ph']]
'''
names4 = copy.deepcopy(names)
print('deepcopy-----',names)
print('deepcopy-----',names4)

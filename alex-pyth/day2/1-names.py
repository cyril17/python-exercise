
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

names3 = names.copy()
print(names3)names[1]=666
print(names,names3)

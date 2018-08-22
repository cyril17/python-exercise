
import shelve
import datetime

d = shelve.open('shelve_test')

# info = {'age':22,'job':'it'}
#
# name = ['gsy','rain','sun']
#
# d['name'] = name   #持久dict
# d['info'] = info   #持久列表
# d['date'] = datetime.datetime.now()
#
# d.close()

print(d.get('name'))
print(d.get('info'))
print(d.get('date'))

'''
['gsy', 'rain', 'sun']
{'age': 22, 'job': 'it'}
2018-07-05 README.md:01:22.940575
'''



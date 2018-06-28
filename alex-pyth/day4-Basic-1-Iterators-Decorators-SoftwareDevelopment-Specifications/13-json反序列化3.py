import json    #pickle只能在Python中使用

f  = open("test.txt","r")

#data = pickle.loads(f.read())

data = json.load(f)  #同data = pickle.loads(f.read()) 一样

print(data['func']('GSY'))

f.close()
'''
helo2 GSY
None
'''


#记得写程序每次dump一次，load一次，
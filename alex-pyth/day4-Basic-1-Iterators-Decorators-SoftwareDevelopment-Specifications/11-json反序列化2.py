import pickle    #pickle只能在Python中使用

def sayhi(name):
    print('helo2',name)     #即使内容不一样，只要函数名一样。就可以反序列化

f  = open("test.yaml.txt","rb")

#data = pickle.loads(f.read())

data = pickle.load(f)  #同data = pickle.loads(f.read()) 一样

print(data['func']('GSY'))

f.close()
'''
helo2 GSY
None
'''

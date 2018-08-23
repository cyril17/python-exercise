import pickle


def sayhi(name):
    print('helo',name)

info = {
    'name':'gsy',
    'age':22,
    'func':sayhi
}

f  = open("test.yaml.txt","wb")
print()
#f.write(pickle.dumps(info))  #直接读取info，write是不支持字典的，通过json.dump转换为字符串，
pickle.dump(info,f)     #等同于f.write(pickle.dumps(info))

f.close()
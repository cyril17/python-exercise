import json


def sayhi(name):
    print('helo',name)

info = {
    'name':'gsy',
    'age':22,
#    'func':sayhi
}

f  = open("test.yaml.txt","w")
print()
f.write(json.dumps(info))  #直接读取info，write是不支持字典的，通过json.dump转换为字符串，

info['age'] = 21

f.write(json.dumps(info))  # XIUG修改值后还是可以通过json读取写入

f.close()

'''
{"name": "gsy", "age": 22}{"name": "gsy", "age": 21}
'''
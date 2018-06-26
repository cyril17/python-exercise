

arg = {
    'bakend': 'www.123.com',
    'record':{
    'server': '100.1.7.9',
    'weight': 20,
    'maxconn': 30}
    }

#exit_flag = False

u_item = input('请输入域名：')

for k,v in arg.items():
    if arg[k] == u_item:
        print(arg)
        arg.pop('bakend')
        print(arg)

#while not exit_flag:

'''
u_item = input("请输入域名：")
for k in arg:
    if arg[k] == u_item:
'''


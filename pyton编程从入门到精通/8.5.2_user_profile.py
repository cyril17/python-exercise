#有时候，需要接受任意数量的实参，但是不知道用户输入什么类型的，这时可将函数编写成可以接受任意数量的的键值对
def build_profile(first,last,**user_info):
    profie = {}
    profie['first_name'] = first
    profie['last_name'] = last

    for key,value in user_info.items():
        profie[key] = value
    return profie

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

def build_profile(**user_file):
    profile = {}
    for key,value in user_file.items():
        profile[key] = value
    return profile
cyril = build_profile(location='princeton',field='physics')
print(cyril)
'''
运行结果
{'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
{'location': 'princeton', 'field': 'physics'}
'''
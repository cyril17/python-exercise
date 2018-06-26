


def test5(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])

test5(name='gsy',age='8',sex='M')

'''
{'name': 'gsy', 'age': '8', 'sex': 'M'}
gsy
8
M
'''

def test6(name,sex,*args,**kwargs):
    print(name,sex,args,kwargs)

test6('gsy','m',num='3655',gf='tt')
test6('gsy','m','666',num='3655',gf='tt')

'''
gsy m () {'num': '3655', 'gf': 'tt'}
gsy m ('666',) {'num': '3655', 'gf': 'tt'}
'''

# -*- coding: utf-8 -*-

import yaml

data = {'name':'johnson', 'age':23,
        'spouse':{'name':'Hallie', 'age':23},
        'children':[{'name':'Jack', 'age':2}, {'name':'Linda', 'age':2}]}

with open('test2.yaml','w') as f:
    f.write(yaml.dump(data))
    print(yaml.dump(data))

'''
age: 23
children:
- {age: 2, name: Jack}
- {age: 2, name: Linda}
name: johnson
spouse: {age: 23, name: Hallie}
'''
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
print(root)
print(root.tag)
'''
<Element 'data' at 0x10b669ae8>
data     返回标签名
'''

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)   #打印标签和属性
    for i in child:
        print(i.tag, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)

'''
country {'name': 'Liechtenstein'}
rank 2
year 2008
gdppc 141100
neighbor None
neighbor None
country {'name': 'Singapore'}
rank 5
year 2011
gdppc 59900
neighbor None
country {'name': 'Panama'}
rank 69
year 2011
gdppc 13600
neighbor None
neighbor None
year 2008
year 2011
year 2011
'''
product_list = [
    ('iphone',5800),
    ('mac pro',9800),
    ('bike',800),
    ('watch',10600),
    ('coffee',31)
]

for index,item in enumerate(product_list):
    print(index,item)

print(product_list[0])

for item in product_list:
    print(product_list.index(item))

#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。




#------------------------------------------------
#关系集合



list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)    #把列表转换为集合

print(list_1,type(list_1))
##{1, 3, 4, 5, 6, 7, 9} <class 'set'>

list_2 = set([2,6,0,66,22,8,4])
print(list_1,list_2)
##{1, 3, 4, 5, 6, 7, 9} {0, 2, 66, 4, 6, 8, 22}

#交集
print(list_1.intersection(list_2))
print(list_1 & list_2)
##{4, 6}


#并集
print(list_1.union(list_2))
print(list_1 | list_2)
##{0, 1, 2, 3, 4, 5, 6, 7, 66, 9, 8, 22}


#差集---in  1  but  not  2
print(list_1.difference(list_2))
print(list_1 - list_2)
##{1, 3, 5, 7, 9}

#子集
print(list_1.issubset(list_2))
#False

#父集
print(list_1.issuperset(list_2))
#False


list_3 = set([4,6])

print(list_1.issuperset(list_3))
#true
print(list_3.issubset(list_2))
#true

#对称差集--symemtric-对称---把交集去掉，剩下的全部合为一个集合
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)
#{0, 1, 2, 66, 3, 5, 7, 8, 9, 22}

#如果2个集合没有交集，则返回true
list_4 = set([1,3,7])
print(list_3.isdisjoint(list_4))
#True


#----------------------------------------------------------------
#其他

# 增加
list_4.add(999)
print(list_4)
##{999, 1, 3, 7}

#增加多个元素
list_4.update([22,33,55])
print(list_4)

#判断集合中元素的个数，集合的长度
print(len(list_4))

#判断元素是否在集合中，
print(33 in list_4)
print(33 not in list_4)

#删除一个元素
list_4.remove(999)
print(list_4)


#随机的删除一个元素
print(list_4.pop())
print(list_4.pop())
print(list_4.pop())

print(list_1)
list_1.discard("444")
#remove删除一个不存在的值会报错，但是discard不会报错





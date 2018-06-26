
info = {
    'stu1102':'LongZe LuoLa',
    'stu1103': 'XiaoZe Maliya',
    'stu1106': 'Alex'
}

print(info)
b = {1:2,3:4,"stu1102":"泷泽萝拉"}
info.update(b)
print(info)
#﻿#update   将2个字典合并，如果有交叉，就合并更新
#输出：
#{'stu1102': 'LongZe LuoLa', 'stu1103': 'XiaoZe Maliya', 'stu1106': 'Alex'}
#{'stu1102': '泷泽萝拉', 'stu1103': 'XiaoZe Maliya', 'stu1106': 'Alex', 1: 2, 3: 4}

print(info.items())
###dict_items([('stu1102', '泷泽萝拉'), ('stu1103', 'XiaoZe Maliya'), ('stu1106', 'Alex'), (1, 2), (3, 4)])

#c = dict.fromkeys([6,7,8])
#print(c)
c = dict.fromkeys([6,7,8],[1,{"name":"cyril"},444])
print(c)
##{6: [1, {'name': 'cyril'}, 444], 7: [1, {'name': 'cyril'}, 444], 8: [1, {'name': 'cyril'}, 444]}
c[7][1]["name"] = "gsy"
print(c)
##{6: [1, {'name': 'gsy'}, 444], 7: [1, {'name': 'gsy'}, 444], 8: [1, {'name': 'gsy'}, 444]}



##简单实现sed功能
with open('17-yesterday','r+',encoding='utf-8') as f1,open('17-yesterday.bak','w',encoding='utf-8') as f2:
    old_str = input("please input you replace str:")
    new_str = input("please input you new str:")

    for line in f1.readlines():
        if old_str in line:
            line = line.replace(old_str,new_str)
            f2.write(line)
            print('你替换的内容为：',line)
    f2.flush()

'''
f = open('17-yesterday','r',encoding='utf-8')
f2 = open('17-yesterday.bak','w',encoding='utf-8')
old_str = input('请输入要修改的字符：')
replace_str = input('请输入替换成的字符:')
for line in f.readlines():
 line = line.replace(old_str,replace_str)
 print(line)
 f2.write(line)
f.close()
f2.close()
f2.flush()
'''
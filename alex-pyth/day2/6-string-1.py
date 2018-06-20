

name = "my name is {0} and i am {1} old"

print(name.capitalize()) #首字母大写
print(name.count("y"))
print(name.center(50,"-"))  #
print(name.endswith("il"))
print(name.expandtabs())
print(name.find('good'))
print(name[name.find("cyril"):])  #相当于字符串的切片，
#print(name.format(name='gsy',year='22'))
print(name.format('gsy',22))
#print(name.format_map({'name':'gsy','year':22}))
print(name.index("is"))
print('￥'.isalnum())
print('sjakA'.isalpha())   #判断是否是字母
print('1A'.isdecimal())    #判断是否是十进制
print('1A'.isdigit())
print('a1A'.isidentifier())  #判断是否是一个合法的标识符，即判断是否是一个合法的变量名
print('A'.isupper())
print('A'.islower())

print('#'.join(['1','2','3','hello']))    #将列表转换成字符串

print('dadsadsads'.rjust(40,'-'))
print('----')
print('  Alpha'.lstrip())
print('----')
#print("this is string example....wow!!!".translate("aeiou","12345"))
#print("this is string example....wow!!!".maketrans("aeiou","12345"))
p = str.maketrans("abcdef",'123456')
print("alex li".translate(p))
#1l5x li


print('gsy cyril'.split())   #按照空格将字符串分成列表，结果['gsy', 'cyril']
print('1+2+3+4'.split('+'))   #按照+将字符串分成列表，结果﻿['1', '2', '3', '4']
print('1+2\n+3+4'.splitlines())   #按照换行符将字符串分成列表，结果['1+2', '+3+4']



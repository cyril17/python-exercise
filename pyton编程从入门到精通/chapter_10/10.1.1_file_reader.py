'''打开文件并且读取全部内容，且打印'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())

str1 = "0000    99    0000"
str2 = "      0000    99    0000    "

print(str1.strip('0'))
print(str2.lstrip())
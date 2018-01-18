filename = 'pi_million_digits.txt'
'''判断生日是否在圆周率中'''
with open(filename) as fi_object:
    lines = fi_object.readlines()

pi_string_birthday = ''
for line in lines:
    pi_string_birthday += line.strip()

birthday = input("please input your birthday,in the from mmddyy:")
if birthday in pi_string_birthday:
    print("you birthday appears in first million digits of pi!")
else:
    print("you birthday does not in the first million digits of pi!")
filename = 'pi_digits.txt'
'''python读取文件的时候默认将所有文本解读为字符串，如果要使用其他格式，需转换'''
with open(filename) as fil_object:
    lines = fil_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

'''
运行结果
3.14159263589793238462643383279
31
'''
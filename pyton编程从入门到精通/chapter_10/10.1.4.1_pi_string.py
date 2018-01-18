filename = 'pi_digits.txt'
'''将文件的每行存储在一个列表中，方便with代码外调用'''
with open(filename) as fil_object:
    lines = fil_object.readlines()

for line in lines:
    print(line.strip())

'''
运行结果
3.141592635
8979323846
2643383279
'''
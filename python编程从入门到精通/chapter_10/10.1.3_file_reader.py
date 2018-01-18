filename = 'pi_digits.txt'
'''逐行读取文件'''
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

'''
源文件
pi_digits.txt
  3.141592635
    8979323846
    2643383279

运行结果
3.141592635
8979323846
2643383279
'''
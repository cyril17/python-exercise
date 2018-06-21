
'''
f = open("11-lyrics",'r+',encoding="utf-8")  #文件句柄，包含文件的名字大小字符集内容内存起始位置


#截取10个字符
#f.seek(10)
#f.truncate(20)
#保留10个字符，从第10个开始截取


print(f.readline())
print(f.readline())
print(f.readline())

print(f.tell())
f.write("--------------")

print(f.readline())
'''



'''
#写读模式没啥用
f = open("11-lyrics",'w+',encoding="utf-8")  #文件句柄，包含文件的名字大小字符集内容内存起始位置
print(f.readline())
print(f.readline())
print(f.readline())

print(f.tell())
f.write("--------------")

print(f.readline())
'''


f = open("11-lyrics",'wb')  #文件句柄，包含文件的名字大小字符集内容内存起始位置

f.write("hello binary\n".encode())
f.close()



f = open("11-lyrics",'a',encoding="utf-8")  #文件句柄，包含文件的名字大小字符集内容内存起始位置

print(f.tell())
print(f.readline())
print(f.readline())
print(f.readline())
#print(f.read(5))
print(f.tell())

#tell就是按照字符来计数的




'''
0
﻿Somehow, it seems the love I knew was always the most destructive kind

不知为何，我经历的爱情总是最具毁灭性的的那种

Yesterday when I was young

168
'''

f.seek(0)
#如果有seek，则下面readline读取的时候还是从第一行开始读
#如果没有seek，则下面读的时候则继续读下一行

print(f.readline())

##﻿Somehow, it seems the love I knew was always the most destructive kind

#输出文本的编码格式
print(f.encoding)
##utf-8

#返回文本在操作系统中的编号
print(f.fileno())
##3

#打印文件名字
print(f.name)
##11-lyrics

#判断是不是终端设备
print(f.isatty())

#判断能不能移
print(f.seekable())

#判断文件是否可读
print(f.readable())

#等缓存写满了只后才会写到硬盘中，刷新一下就相当于写到了硬盘中，强制刷新
print(f.flush())
















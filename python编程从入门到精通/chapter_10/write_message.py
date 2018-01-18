filename = 'programming.txt'
'''将文本写入文件，python只能将字符串写入文件，要将数值写入文件，需要先用str()转换为字符串'''

with open(filename,'w') as file_object:
      file_object.write("i love you")

'''
运行结果
programming.txt  将会追加刚才添加的文本
'''
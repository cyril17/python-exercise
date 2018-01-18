filename = 'alice.txt'
'''
此处如果文件不存在，则会提示文件不存在
Traceback (most recent call last):
  File "D:/python-exercise/python编程从入门到实践/chapter_10/alice.py", line 3, in <module>
    with open(filename) as file_object:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
'''
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("the file " + filename + " not exist")
else:
    words = contents.split()
    news_world = len(words)
    print("This file" + filename + "has" + news_world + "worlds.")
'''
运行结果
the file alice.txt not exist
'''
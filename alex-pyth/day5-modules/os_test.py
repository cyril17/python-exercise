# -*- coding: utf-8 -*-

import  os

print(os.path)
#<module 'posixpath' from '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/posixpath.py'>
print(os.getcwd())
#/Users/cyril/Documents/python-exercise/python-exercise/alex-pyth/day5-modules
#print(os.chdir('/'))
print(os.getcwd())
print(os.pardir)
print(os.getcwd())
#os.makedirs('a/b/c')   #递归创建删除目录
#os.removedirs('a/b/c')

# os.rmdir('bb')
# os.rmdir('aa')
#删除单个目录
print(os.listdir('./'))
#['random_test.py', 'module_2.py', '__pycache__', 'os_test.py', '1-模块介绍.py', 'time_test.py', 'module_1.py']
#列出当前目录下的所有文件或者子目录
print(os.stat('./os_test.py'))
#os.stat_result(st_mode=33188, st_ino=2987780, st_dev=16777223, st_nlink=1, st_uid=503, st_gid=20, st_size=706, st_atime=1530699788, st_mtime=1530699788, st_ctime=1530699788)
#获取文件或者目录的信息

print(os.name)
#posix

print(os.environ)   #获取系统环境变量
'''
environ({'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/VMware Fusion.app/Contents/Public:/Applications/Wireshark.app/Contents/MacOS:.', 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk1.8.0_172.jdk/Contents/Home', 'LOGNAME': 'cyril', 'XPC_SERVICE_NAME': 'com.jetbrains.pycharm.4104', 'PWD': '/Users/cyril/Documents/python-exercise/python-exercise/alex-pyth/day5-modules', 'PYCHARM_HOSTED': '1', 'PYCHARM_MATPLOTLIB_PORT': '60279', 'PYTHONPATH': '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend:/Users/cyril/Documents/python-exercise/python-exercise', 'SHELL': '/bin/zsh', 'PAGER': 'less', 'LSCOLORS': 'Gxfxcxdxbxegedabagacad', 'PYTHONIOENCODING': 'UTF-8', 'OLDPWD': '/Applications/PyCharm.app/Contents/bin', 'USER': 'cyril', 'ZSH': '/Users/cyril/.oh-my-zsh', 'TMPDIR': '/var/folders/3p/tfx9b6v50mb1pqh_fv0rx3bw0000gq/T/', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.RXBKafOoMY/Listeners', 'XPC_FLAGS': '0x0', 'PYTHONUNBUFFERED': '1', 'MYSQL_HOME': '/usr/local/mysql/bin', '__CF_USER_TEXT_ENCODING': '0x1F7:0x19:0x34', 'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.1Rp3FcsBD2/Render', 'LESS': '-R', 'LC_CTYPE': '', 'HOME': '/Users/cyril', '__PYVENV_LAUNCHER__': '/usr/local/Cellar/python/3.6.5/bin/python3'})

'''

#文件的绝对路径
print(os.path.abspath(__file__))

print(os.path.split(r'/Users/cyril/test.yaml/a/b/b.txt'))
#('/Users/cyril/test.yaml/a/b', 'b.txt')
#将path分割成目录和文件名二元组返回

print(os.path.dirname(r'/Users/cyril/test.yaml/a/b/b.txt'))
#/Users/cyril/test.yaml/a/b
#﻿返回path的目录。其实就是os.path.split(path)的第一个元素

print(os.path.basename(r'/Users/cyril/test.yaml/a/b/b.txt'))
#b.txt
#﻿返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素

print(os.path.exists(r'/Users/cyril/test.yaml/a/b'))   #﻿如果path存在，返回True；如果path不存在，返回False

#False

print(os.path.exists('/Users/cyril/'))   #﻿如果path存在，返回True；如果path不存在，返回False

print(os.path.isabs(r'test.yaml/a/b'))   #﻿如果path存在，返回True；如果path不存在，返回False
#False

print(os.path.isfile(r'/Users/cyril/test.yaml/a/b/b.txt'))   #﻿如果path存在，返回True；如果path不存在，返回False
print(os.path.isdir(r'/User/cyril/test.yaml/a/b'))   #﻿如果path存在，返回True；如果path不存在，返回False


print(os.path.join(r'/User/cyril/','test.yaml'))   #﻿如果path存在，返回True；如果path不存在，返回False
#/User/cyril/test.yaml

print(os.path.getatime(r'/Users/cyril/'))
#1530712042.0941296
#最后访问时间
print(os.path.getmtime(r'/Users/cyril/'))
#最后修改时间


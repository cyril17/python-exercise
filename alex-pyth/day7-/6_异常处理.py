# -*- coding: utf-8 -*-

num = [1,2,3]
name = {}

try:
    name['name']
    print(num[4])

except KeyError as e:
    print('没有这个key',e)
#没有这个key 'name'

except IndexError as f:
    print('没有此')

#也可以这样
#except (KeyError,IndexError) as e:

except Exception as e:   #只要抛出错误，就执行，一般前面抓不到指定的错误类型就写这个，
    print('未知错误：',e)


else:
    print('一切正常')    #没出错的时候执行这个
finally:
    print('不管有错没错都执行此')
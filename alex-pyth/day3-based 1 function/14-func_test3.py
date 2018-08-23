

def test(x,y):
    print(x)
    print(y)

#x,y为形参，
test(1,3)   #实参跟形参一一对应，位置参数
test(y=1,x=3)   #实参跟形参，与位置无关，关键字调用


test(1,y=3)   #实参跟形参一一对应，位置参数

#下面错误
#test.yaml(x=1,3)
#test.yaml(1,x=3)

#关键参数是不能写在位置参数前面的
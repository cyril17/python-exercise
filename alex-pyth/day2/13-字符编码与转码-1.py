
#
def func1():
    """test1"""
    print("in the func1")
    return 0

#过程，过程返回值为空
def func2():
    """test2"""
    print("in the func2")

x = func1()
y = func2()

print("func1 return :",x)
print("func2 return :",y)
'''
in the func1
in the func2
func1 return : 0
func2 return : None
'''




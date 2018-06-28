

def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar() #此处如果不写，在运行的时候就不运行bar


foo()
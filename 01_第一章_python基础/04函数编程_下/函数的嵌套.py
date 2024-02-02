"""
函数可以嵌套函数 但是不可以嵌套类
函数可以作为参数传递给另外一个函数
函数可以作为返回值返回 但是类不可以
函数名是一个变量，函数名可以作为变量使用
"""


def f1():
    print('f1')

    def f2():  # f2是f1的局部变量
        print('f2')

    f2()  # 调用f2 f2是局部变量，只能在f1内部使用


f1()


def func1():
    print('func1')

    def func2():
        print('func2')

    return func2  # 返回的是一个函数对象 func2是局部变量，只能在func1内部使用 func1()返回的是一个函数对象，再次调用这个函数对象 func1()() 调用func2


func1()()  # func1()返回的是一个函数对象，再次调用这个函数对象 func1()() 调用func2


# 代理模式 一个函数的参数是另外一个函数
def func3(an):
    an()  # 调用an函数


def target():
    print("我是target函数")


c = 454
func3(target)  # func3(target) target是一个函数对象，传递的是一个函数对象

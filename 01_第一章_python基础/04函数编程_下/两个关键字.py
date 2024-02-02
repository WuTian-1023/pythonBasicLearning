"""
global关键字 作用：在函数内部声明全局变量
nonlocal关键字 作用：在函数内部声明外部嵌套函数的变量，只能在内部嵌套函数中使用，不能在函数内部使用
"""
a = 1


def func():
    # a = 10 # 局部变量 作用域是函数内部 不能在函数外部使用，并没有改变全局变量的值
    # print(a)
    global a  # 使用global关键字声明为全局变量
    a = 20  # 修改全局变量的值
    print(a)


func()
print(a)


def func2():
    b = 10

    def func3():
        nonlocal b  # 使用nonlocal关键字声明为外部嵌套函数的变量
        b = 20  # 修改外部嵌套函数的变量的值
        print(b)

    func3()
    print(b)

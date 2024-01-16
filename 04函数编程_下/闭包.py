"""
闭包：内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包
    1.可以让一个变量常驻内存
    2.可以将一个局部变量的生命周期延长
    3.可以避免全局变量的污染---->封装
"""


def func():
    a = 10

    def inner():
        nonlocal a
        a += 1
        return a

    return inner


inner = func()
i = inner()
print(i)

i2 = inner()
print(i2)

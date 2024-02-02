"""
匿名函数：
    lambda 表达式
    语法：
       变量 =  lambda 参数列表：返回值

"""


def add(x, y):
    return x + y


ret = add(2, 3)
print(ret)

ret = lambda x, y: x + y
print(ret(2, 3))

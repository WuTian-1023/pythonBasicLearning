
"""
返回值：函数执行完成之后，返回给调用者的结果
关于return
    1.如果函数没有返回值，那么默认返回None
    2.如果函数有返回值，那么返回值的类型，取决于return后面的值的类型
    3.如果函数有返回值，那么return后面的代码不会执行
    4.如果函数有返回值，那么return后面可以不跟任何的值，这个时候，函数返回None
    5.如果函数有返回值，那么return后面可以跟多个值，这个时候，返回的是一个元组
"""

def add(a, b):
    return a + b

num = add(1, 2)

print(num)

def add2():
    return 1, 2, 3, 4, 5

num2 = add2()
print(num2)
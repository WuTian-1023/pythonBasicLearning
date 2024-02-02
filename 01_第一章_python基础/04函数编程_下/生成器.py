"""
生成器：
    生成器是一个特殊的迭代器
    创建生成器的方式：
        1. 生成器表达式：一次性的，用完就扔
        2. yield关键字

    生成器函数：
        1.函数体内有yield关键字
        2.调用函数得到的返回值是一个生成器

        yield:只要函数体内有yield关键字，那么这个函数就是一个生成器函数
            作用：
                1.可以让函数暂停
                2.可以保存函数的运行状态
                3.可以让函数从暂停的地方继续执行
                4.可以返回值
                5.可以分段执行函数体代码，通过__next__方法控制
        优势：
            节省内存空间
"""


# yield关键字
def func():
    print("我是第一次调用")
    yield 1
    print("我是第二次调用")
    yield 2
    print("我是第三次调用")
    yield 3


ret = func()  # 调用函数，函数内部的代码不会执行，返回值是一个生成器
print(ret.__next__())  # 通过生成器调用__next__方法，函数内部的代码开始执行，遇到yield关键字停止，返回yield后面的值
print(ret.__next__())


# 去工厂定制10000件衣服
def order():
    lst = []
    for i in range(10000):
        lst.append("衣服%s" % i)
        if len(lst) == 100:
            yield lst
            lst = []
    return lst


generator = order()
print(generator.__next__())
print(generator.__next__())

# 生成器表达式
range_ = (i ** 2 for i in range(10))
# for i in range_:
#     print(i)

lst = list(range_)  # 上面的循环已经把生成器里面的数据取完了，所以这里的lst是空的，不信你就试试
print(lst)

s = list("周杰伦")  # 字符串也是可迭代对象 list() => for => next()
print(s)

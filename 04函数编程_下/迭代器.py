"""
for 变量 in 可迭代
    语句  # 可迭代对象中的每个元素都会被迭代器取出来，赋值给变量，然后执行语句

iterable: 可迭代对象
str list tuple dict set open()
可迭代的数据类型都会提供一个叫迭代器的东西，用来迭代数据可以帮我们把数据类型里的所有数据逐一取出来

获取迭代器的方法：
                1.iter(可迭代对象)
                2.可迭代对象.__iter__()
"""
# for c in "hello":
#     print(c)

i = iter("hello")
print(next(i))

iter__ = "呵呵哒".__iter__()
print(next(iter__))

# 模拟for循环
"""
for里面一定是要拿到迭代器的，然后不断的调用next方法，直到捕获到StopIteration异常
总结：迭代器统一了不同数据类型的取值方式，迭代器可以统一不同数据类型的取值方式
"""


def my_for(iterable):
    iterator = iterable.__iter__()
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            break


my_for("hello")

"""
 迭代器本身是可以迭代的，迭代器里面的数据是惰性的，只有调用next方法的时候才会取值
 本身的特性：
            1.只能向前不能反复只能取一次  
            2.节省内存空间
            3.数据是惰性的
"""


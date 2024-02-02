"""
递归： 函数调用自身的编程技巧称为递归（recursive）
python对递归深度有限制，超过限制报错 RecursionError: maximum recursion depth exceeded while calling a Python object
默认的递归深度是1000，超过限制报错
"""
import sys

# def func():
#     print("我是func函数")
#     func()
#
#
# func()  # RecursionError: maximum recursion depth exceeded while calling a Python object 递归深度超过最大限制

print(sys.getrecursionlimit())  # 获取递归深度
sys.setrecursionlimit(1500)  # 设置递归深度
print(sys.getrecursionlimit())

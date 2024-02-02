"""
    异常：
"""
# 1.异常的概念
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("除数不能为0。")
    return x / y

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)  # 打印异常信息：除数不能为0。


divide(0, 1)

# 2.异常的处理
def error():
    try:
        print(1/0)
    except:
        print("我是异常后面的代码")

error()


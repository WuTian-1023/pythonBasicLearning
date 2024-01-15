"""
函数：对某一个特定的功能进行封装，使得代码更加简洁，提高代码的复用性

定义：
    def 函数名(参数列表):
        函数体

调用：
    函数名(参数列表)

好处：
    1.提高代码的复用性
    2.使得代码更加简洁

参数：可以在函数调用的时候，给函数传递一些信息，这些信息就是参数
    分类：
    1.形参：定义函数的时候，小括号中的参数，用来接收参数用的
        1.位置参数，必须传递，而且位置要对应
        2.默认参数，可以不传递，不传递的时候使用默认值
    2.实参：调用函数的时候，小括号中的参数，用来传递给函数的实际数据
        1.位置参数，必须传递，而且位置要对应
        2.关键字参数，可以不传递，不传递的时候使用默认值
        3.混合参数，位置参数必须在关键字参数的前面

"""


def myPrint():
    print("hello world")


myPrint()


def myPrint2(name, age):
    print(f"我叫： {name}, 我的年龄是：{age}")


myPrint2("张三", 18)


# 编写一个计算器  计算四则运算
def calculator(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("输入的运算符有误")


calculator(1, 89, "/")
calculator(num2=1, num1=89, operator="/")


# 默认参数
def myPrint3(name, age=18, gender="男"):
    print(f"我叫： {name}, 我的年龄是：{age}, 我的性别：{gender}")


myPrint3("张三")





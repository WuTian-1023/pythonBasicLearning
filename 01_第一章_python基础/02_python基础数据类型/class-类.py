# --*-- conding:utf-8 --*--
# @Time : 2024-01-31 031 下午 03:02
# @Author : CoderTLL
# @Email : javacoder1023@gmail.com
# @File : class-类.py
# @Software : PyCharm
# 代码不规范 同事两行泪

"""
 python的类
    1.类的定义
    2.类的实例化
    3.类的属性
    4.类的方法
    5.类的继承
    6.类的多态
    7.类的私有属性和私有方法
    8.类的特殊方法
    9.类的魔术方法
    10.类的装饰器
    11.类的静态方法和类方法
    12.类的__slots__属性
    13.类的__new__方法
    14.类的__call__方法
    15.类的__str__方法
    16.类的__repr__方法
    17.类的__getitem__方法
    18.类的__setitem__方法
    19.类的__delitem__方法
    20.类的__getattr__方法
    21.类的__setattr__方法
    22.类的__delattr__方法
    23.类的__getattribute__方法
    24.类的__len__方法
    25.类的__iter__方法
    26.类的__next__方法
    27.类的__contains__方法
    28.类的__enter__方法
    29.类的__exit__方法
    30.类的__add__方法
    31.类的__sub__方法
    32.类的__mul__方法
    33.类的__truediv__方法
    34.类的__floordiv__方法
    35.类的__mod__方法
    36.类的__pow__方法
    37.类的__and__方法
    38.类的__or__方法
    39.类的__xor__方法
    40.类的__lshift__方法
    41.类的__rshift__方法
    42.类的__iadd__方法
    43.类的__isub__方法
    44.类的__imul__方法
    45.类
"""


# 类定义：使用class关键字定义类，后跟类名和冒号。类名通常采用驼峰命名法。
class MyClass:
    pass


# 类的实例化：创建类的实例（对象）是通过调用类名作为函数来完成的。
my_instance = MyClass()


# 类的属性：类的属性是在类定义中定义的变量。它们代表了类的状态或数据
class MyClass:
    my_attribute = 123


# 类的方法：类的方法是在类定义中定义的函数。它们代表了类的行为或功能。
class MyClass:
    def my_method(self):
        print("Hello, World!")


#  类的继承：一个类可以继承另一个类的属性和方法，这被称为类的继承。继承的类被称为子类，被继承的类被称为父类。
class MyParentClass:
    pass


class MyChildClass(MyParentClass):
    pass


# 类的多态：多态是指一个类的实例（对象）可以在不同的类中表现出不同的行为。
class MyParentClass:
    def my_method(self):
        print("Parent method")


class MyChildClass(MyParentClass):
    def my_method(self):
        print("Child method")


# 类的私有属性和私有方法：私有属性和方法是在类定义中定义的属性和方法，它们不能从类的外部访问。
class MyClass:
    __private_attribute = 123  # 私有属性 __private_attribute

    def __private_method(self):
        print("Private method")

    def public_method(self):
        print("Public method")
        # 在类的内部，我们可以访问私有属性和方法
        print(self.__private_attribute)
        self.__private_method()



my_class = MyClass()
my_class.public_method()  # 输出：Public method 123 Private method
# 类的特殊方法：特殊方法是在类定义中定义的方法，它们具有特殊的名称。它们通常被称为魔术方法。
class MyClass:
    def __init__(self):
        print("Constructor called, object created.")

    def __del__(self):
        print("Destructor called, object destroyed.")


my_instance = MyClass()  # 输出：Constructor called, object created.
del my_instance  # 输出：Destructor called, object destroyed.
"""
在Python中，魔术方法是一种特殊的方法，它们的名称以双下划线开始和结束，
如`__init__`、`__str__`等。这些方法在特定的情况下会被Python自动调用，
因此它们也被称为特殊方法或者魔术方法。

以下是一些常见的魔术方法及其用途：

1. `__init__`：这是类的构造方法，当创建类的新实例时，它会被自动调用。

2. `__del__`：这是类的析构方法，当类的实例被销毁时，它会被自动调用。

3. `__str__`：当我们使用`print`函数打印类的实例，或者使用`str`函数将类的实例转换为字符串时，这个方法会被调用。

4. `__eq__`、`__ne__`、`__lt__`、`__gt__`、`__le__`、`__ge__`：这些方法用于重载比较运算符，使得我们可以使用比如`==`、`!=`、`<`、`>`、`<=`、`>=`等运算符来比较类的实例。

5. `__add__`、`__sub__`、`__mul__`、`__truediv__`等：这些方法用于重载数学运算符，使得我们可以使用`+`、`-`、`*`、`/`等运算符来操作类的实例。

这些魔术方法使得我们可以自定义类的行为，使其更符合我们的需求。
"""


# 类的装饰器
class MyClass:
    @classmethod
    def my_class_method(cls):
        print("Class method")

    @staticmethod
    def my_static_method():
        print("Static method")


MyClass.my_static_method()  # Static method
MyClass.my_class_method()  # Class method

"""
在Python中，被@staticmethod或@classmethod装饰的方法，
可以直接通过类名来调用，而不需要创建类的实例。这两种方法都属于类级别的方法，
而不是实例级别的方法。

在Python中，类的普通方法（非静态方法和类方法）在被调用时，
Python会自动传入一个隐式参数，通常我们将这个参数命名为self。
这个self参数代表了类的实例。例如：
    class MyClass:
    def my_method(self):
        print("This is a method.")
    
    my_instance = MyClass()
    my_instance.my_method()  # 输出：This is a method.

在上述代码中，我们没有显式地为my_method方法的self参数传入值，
Python自动为我们做了这件事。这个self参数就代表了调用方法的实例my_instance。
"""

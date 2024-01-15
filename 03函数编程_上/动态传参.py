
# 动态传参
# *args 会把多余的位置参数，转换成一个元组
# *args 要在默认参数前面
# **kwargs 会把多余的关键字参数，转换成一个字典
# 注意：*args必须在**kwargs的前面
# 顺序：位置参数, *args , 默认参数, **kwargs
def myPrint4(a, b, *args, c="哈哈", **kwargs):
    print(a, b, args, c, kwargs)


myPrint4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, c="呵呵", d=1, e=2, f=3, g=4, h=5, i=6, j=7, k=8)

stu_lst = ["刘德华", "张学友", "周杰伦", "张杰"]


def func(*args):
    print(args)


func(*stu_lst)  # *在调用的时候，会把列表中的每一个元素，拆分成一个一个的位置参数 **
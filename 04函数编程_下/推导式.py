"""
推导式：
     简化代码。
     语法：
        列表推导式：[数据 for循环 if判断]
        集合推导式：{数据 for循环 if判断}
        字典推导式：{key:value for循环 if判断}

"""
lst = []
# for i in range(10):
#     lst.append(i)
#
# print(lst)

lst = [i for i in range(10)]
print(lst)

lst = [i for i in range(1, 11) if i % 2 == 1]
print(lst)

# 创建一个列表里面放 1-10的偶数
lst = [i for i in range(1, 11) if i % 2 == 0]
print(lst)

# 创建一个列表里面放 1-10的偶数的平方
lst = [i * i for i in range(1, 11) if i % 2 == 0]
print(lst)

# 创建一个列表里面放50件衣服
lst = ["衣服%s" % i for i in range(50)]
print(lst)

# 创建一个列表中所有的英文单词都是大写
lst = ["hello", "world", "python", "java"]
lst = [i.upper() for i in lst]
print(lst)

# 集合推导式
s = {i for i in range(10)}
print(s)

# 字典推导式
d = {i: i + 1 for i in range(10)}
print(d)

# 将一个字典的key和value对调
d = {"a": 1, "b": 2, "c": 3}
d = {d[key]: key for key in d}
print(d)

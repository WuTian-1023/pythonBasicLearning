"""
内置函数：直接使用，不需要导入
print()
input()
"""
s = "123"
i = int(s)
b = bool(s)
f = float(s)
# complex 复数：实数+虚数

# bin()   二进制
# oct()   八进制
# hex()  十六进制
a = 12  # 十进制
print(bin(a))  # 二进制 0b1100
print(oct(a))  # 八进制 0o14
print(hex(a))  # 十六进制 0xc

print(int("0b1100", 2))  # 二进制转换成十进制

# sum, max, min, len, abs, pow, round, divmod
a = 10
b = 3
print(divmod(a, b))  # (3, 1)  商和余数
print(pow(a, b))  # 1000
print(abs(-10))  # 10
print(round(3.1415926, 2))  # 3.14  四舍五入
print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 55
print(max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 10
print(min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 1
print(len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 10

# format 格式化输出 ord chr
print(format(a, "08b"))  # b:二进制 1010 d:十进制 10  o:八进制 12  x:十六进制 a  X:十六进制 A
print(ord("中"))  # 20013 python内存中，所有的字符串都是以unicode编码的
print(chr(20013))  # 中 unicode编码 给出了所有的字符和二进制之间的对应关系

# for i in range(0, 65536):
#     print(chr(i)+ " ", end="")

# eumrate  all any
lst = [1, 2, 0, 4, 5]
print(all(lst))  # True  所有的元素都是True，那么all的结果就是True
print(any(lst))  # True  只要有一个元素是True，那么any的结果就是True
for index, item in enumerate(lst):
    print(index, item) # 0 1  1 2  2 0  3 4  4 5 返回的是一个元组 元组中第一个元素是索引，第二个元素是值 enumerate 枚举

s = "呵呵哒"
print(hash(s))  # 一个字符串对应一个数字，这个数字是根据字符串的内容计算出来的，这个过程叫做hash
                # hash值是一样的，那么字符串的内容也是一样的

# id()  查看变量的内存地址
a = 10
b = 10
print(id(a))  # 1407079680
print(id(b))  # 1407079680
print(id(10)) # 1407079680  10是一个不可变的数据类型，不管创建多少次，都是同一个对象
print(id("呵呵"))  # 1407079680  字符串也是不可变的数据类型，不管创建多少次，都是同一个对象
print(id([1, 2, 3]))  # 1407079680  列表是可变的数据类型，每一次创建，都是一个新的对象
# id() 查看变量的内存地址

# help  查看帮助文档
# help(print)
# help(str)
# help(list)
# help(tuple)
# help(dict)
# help(set)
# help(int)
# help(float) 查看帮助文档 退出帮助文档：按q 退出 按空格键：向下翻页  按b：向上翻页 按h：查看帮助文档的帮助文档
print(dir(str))  # 查看字符串的所有方法
print(dir(list))  # 查看列表的所有方法




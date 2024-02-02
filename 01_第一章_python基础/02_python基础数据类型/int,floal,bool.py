# int 整数 加减乘除 大小比较
a = 10
# float: 小数，浮点数
print(10 / 3)

# bool : 用于做条件判断
# 取值范围 True ， False
print(type(a))

# 在python中所有非0的数字都是true
b = bool(a)
print(type(b))
print(b)

c = 0
d = bool(c)
print(type(d))
print(d)

# 在python中所有非空字段串都是True 空字符串是false
str = ""
e = bool(str)
print(e)
str = "123123"
f = bool(str)
print(f)
# 在python中表示空的东西都是false 不空的东西都是true
while 1:
    content = input("请输入你要发送的内容：")
    if content:
        print("你发送的：", content)
    else:
        print("交流结束")
        break

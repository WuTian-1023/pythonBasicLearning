# 基础数据类型的转换
a = 10  # 在python中 所以非0的数字都是True 0 是false
b = bool(a)
print(type(b))
print(b)

s = "你好啊"  # 在python中,所有非空的字符串都是True 空字符串是False
print(bool(s))

lst = [0]
print(bool(lst))

while 1:
    content = input("请输入你要发给打野的内容：")
    if content:
        print("你发给打野的内容：", content)
    else:
        break

# 变量 = input(提示语);
a = input("请输入第一个数字")
print(type(a)) # type查看变量的数据类型
b = input("请输入第二个数字")
print(type(b))
# 如何转换数据类型？要变什么类型就用谁包住它强转
print(int(a) + int(b))
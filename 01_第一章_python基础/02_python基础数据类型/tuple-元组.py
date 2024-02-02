# tuple 元组 特点：不可变的列表
t = ("张无忌", "赵敏", "周芷若")
print(t)
print(t[1:3])
# t[0] = "田季明" # TypeError: 'tuple' object does not support item assignment

print(t)
# 固定了某些数据 不允许外界修改
# 元组如果只有一个元素
t = ("呵呵",)
print(t)
print(type(t))
t = ("呵呵")
print(t)
print(type(t))

# 元素的不可变  内存地址不可变 可以加内容
t = (1, 2, 3, ["呵呵呵呵", "摸摸哒"])  #
t[3].append("基尼太美")
print(t)

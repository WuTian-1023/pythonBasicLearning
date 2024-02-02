# set集合 set集合是无序的
s = {}
print(type(s))

s = {1, 2, 3}
print(type(s))

s = {1, 2, 3, "呵呵哒", 4, 6}
print(s)
print(type(s))

# s = {1, 2, 3, "呵呵哒", 4, 6, []}  # TypeError: unhashable type: 'list' 不可哈希类型：“list”
# print(s)
# 不可哈希：python中的set集合进行数据存储的时候 需要对数据进行哈希计算 根据计算出来的哈希值来存储数据
# 要求存储的数据必须是可以进行哈希计算的
# 可变的数据类型：list dict set
# 可哈希：不可变的数据类型 int str tuple bool

s = set()  # 创建空集合
# t = tuple()
# l = list()
# s = str()

# set的增删改查
# 增加
s.add("杨幂")
s.add("宋小宝")
s.add("杨玉环")
print(s)
# 删除
# s.pop() #删除最后一个 但是set是无序的每次删除的数据不会一致
s.remove("杨幂")
print(s)
# 修改 只能先删后加来修改
s.remove("宋小宝")
s.add("马云")
print(s)

# 查询
for item in s:
    print(item)

# 交集 并集 差集
s1 = {"刘能", "赵四", "赵本山"}
s2 = {"刘大能", "赵小四", "赵本山"}
# 交集
print(s1 & s2)
print(s1.intersection(s2))

# 并集
print(s1.union(s2))
print(s1 | s2)

# 差集
print(s1 - s2)
print(s1.difference(s2))

# 集合重要的作用 去重复
lst = ["刘能", "赵四", "赵本山","刘能", "赵四", "赵本山","刘能", "赵四", "赵本山","刘能", "赵四", "赵本山"]
print(lst)
print(list(set(lst))) # 去除重复后的数据是无序的

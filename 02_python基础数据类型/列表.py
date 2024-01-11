# 定义:能装大量的东西
# 在python中用[] 来表示一个列表 列表中的元素用,隔开
a = ["张三丰", "张无忌", "adb", 12312, True]
# 特性:
# 1.也可以索引和切片
# 索引超出范围会越界
lst = ["金毛狮王", "张三", "李斯", "王五"]
for i in range(len(lst)):
    item = lst[i]
    if item.startswith("张"):
        new_name = "王" + item[1:]
        print(new_name)
        lst[i] = new_name

print(lst)

# print(lst[0])
# print(lst[1:3])
# print(lst[::-1])

# for item in lst:
#     print(item)
# print(len(lst))

# 列表的增删改查
lst = []
lst.append("张三")
lst.append("李斯")
lst.append("王五")
print(lst)
# insert() 插入
lst.insert(0, "赵敏")
# extend() 合并两个列表 批量添加
lst.extend(["武则天", "嬴政", "马超"])

# 删除
pop = lst.pop(3)
print(pop)
print(lst)

lst.remove("马超")
print(lst)

# 修改
lst[1] = "凯南"
print(lst)

# 列表的排序
lst = [1, 2, 3, "马云", "马化腾"]
print(lst)
lst = [1, 2, 3, 343, 12, 756]
# 升序
lst.sort()
print(lst)

lst = [1, 2, 3, 343, 12, 756]
# 降序
lst.sort(reverse=True)
print(lst)
# print(lst)
# 重复
# print(['hi!'] * 4)
# 元素是否存在于列表中
# print(3 in [1, 2, 3])
# 组合
# print([1, 2, 3] + [4, 5, 6])
# 集合的长度  len
# print(len([1, 2, 3]))
# 统计某个元素在列表中出现的次数
# print(lst.count("武则天"))
# 反向列表中元素  ['赵敏', '张三', '李斯', '王五', '武则天', '嬴政', '马超'] -> ['马超', '嬴政', '武则天', '王五', '李斯', '张三', '赵敏']
lst.reverse()
# print(lst)
# 如果是字符串的话 Python的默认排序方法是逐个字符比较，从第一个字符开始比较，直到出现不同的字符为止
aList = ['123', 'Google', 'Runoob', 'Taobao', 'Facebook']

aList.sort()
print("List : ")
print(aList)

# 列表
vowels = ['e', 'a', 'u', 'o', 'i']
# 降序
vowels.sort(reverse=True)

# 输出结果
# print('降序输出:')
# print(vowels)

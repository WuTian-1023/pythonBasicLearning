"""
zip:可以把多个可迭代对象打包成一个元组，返回一个可迭代对象
locals:查看当前作用域中的所有变量
globals:查看全局作用域中的所有变量
sorted:排序
filter:过滤
map:映射
"""
# zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回
# 列表长度与最短的对象相同，利用*号操作符，可以将元组解压为列表。
a = [1, 2, 3]
b = ["亚索", "瑞文", "盖伦"]
c = ["男", "女", "男"]
zipped = zip(a, b, c)  # 打包为元组的列表
print(zipped)  # <zip object at 0x103abc288>
print(list(zipped))  # [(1, '亚索', '男'), (2, '瑞文', '女'), (3, '盖伦', '男')]

a = 111
print(locals())  # 查看当前作用域中的所有变量


def func():
    b = 222
    print(locals())  # 查看当前作用域中的所有变量，此时只有b


func()
c = 123
print(globals())  # 查看全局作用域中的所有变量

lst = [12, 3, 4, 5, 6, 7, 8, 9, 0]
# lst = sorted(lst, key=len)
# 排序 默认升序 reverse=True降序
# key=len按照长度排序
# key=str.lower按照字母排序
# key=abs按照绝对值排序
# key=函数名按照函数的返回值排序
lst = sorted(lst, reverse=True)
print(lst)

lst = ["李白", "杜甫", "王安石", "苏轼", "李商隐", "蒙娜丽莎", "张三丰", "易"]


def func(name):
    return len(name)


sort = lambda name: len(name)
sort1 = sort(lst[2])
print(sort1)

i = func(lst[0])
print(i)

lst = sorted(lst, key=lambda name: len(name))  # 按照名字的长度排序
print(lst)

lst = [
    {"id": 1, "name": "周润发", "age": 18, "salary": 30000, "city": "北京"},
    {"id": 2, "name": "周星驰", "age": 28, "salary": 20000, "city": "上海"},
    {"id": 3, "name": "周杰伦", "age": 38, "salary": 10000, "city": "深圳"},
    {"id": 4, "name": "周树人", "age": 48, "salary": 5000, "city": "广州"},
    {"id": 5, "name": "周扒皮", "age": 58, "salary": 2000, "city": "杭州"},
]

# 根据每个人的年龄进行排序
lst = sorted(lst, key=lambda dic: dic["age"])
print(lst)

# 根据每个人的薪资进行排序
lst = sorted(lst, key=lambda dic: dic["salary"], reverse=True)  # 按照薪资降序排序
print(lst)

# filter 过滤
lst = ["李白", "杜甫", "王安石", "苏轼", "李商隐", "蒙娜丽莎", "张三丰", "易"]
lst = filter(lambda name: not name.startswith("李"), lst)
print(list(lst))

# map 映射
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
ret = [item * item for item in lst]
print(ret)

lst = map(lambda item: item * item, lst)  # map函数返回的是一个迭代器
print(list(lst))

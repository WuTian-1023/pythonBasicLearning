# 字典的存储方式 键值对的形式来存储 类似Java的map？？？
# 字典的表示方式 ： {key:value, key2:value, key3:value}
dic = {"jay": "周杰伦", "马化腾": "资本家"}
val = dic["jay"]
print(val)

# 字段的key 必须是可哈希的数据类型
# 字段的value 可以是任何数据类型
# dic = {[]:123}
# print(dic) TypeError: unhashable type: 'list' TypeError：不可哈希类型：“list”

dic = {"资本家的走狗": ["走狗1", "走狗2"]}
print(dic)

# 字典的增删改查
# 增加
dic = dict()
dic['jay'] = "周杰伦"
dic[1] = 123
print(dic)

# 修改
dic['jay'] = "蔡徐坤"
print(dic)
dic.setdefault("ikun", "小黑子")
dic.setdefault("ikun", "基尼太美")
print(dic)

# 删除
dic.pop("jay")
print(dic)

# 查询
print(dic["ikun"])
print(dic.get("ikun"))
print(dic.get("ikun123"))  # kay不存在返回None
# print(dic["ikun12321"])#key不存在 程序报错

# None
a = None  # 单纯表示空 什么都没有
print(type(a))

# 例子
dic = {
    "盖伦": "蹲草大宝剑",
    "皇子": "能击飞盖人",
    "亚索": "eeeeeeee",
    "蛮子": "五秒真男人",
}
name = input("你要选择的LOL英雄：")
val = dic.get(name)
if val is None:
    print("该角色还没上线！")
else:
    print(val)

# 字典的循环
for key in dic:
    print(key, dic[key])

# 获取所有的key
print(list(dic.keys()))

# 获取所有的value
print(list(dic.values()))

# 获取所有的key 和 value
print(dic.items())
for item in dic.items():
    key = item[0]
    value = item[1]
    print(key, value)

# 解包
for key, value in dic.items():
    print(key, value)

# 字典的嵌套
wangfeng = {
    "name": "汪峰",
    "age": 16,
    "wifi": {
        "name": "章子怡",
        "hobby": "演戏",
        "assistant": {
            "name": "樵夫",
            "age": 10,
            "hobby": "打游戏"
        }
    },
    "children": [
        {
            "name": "AAA", "age": 1
        }, {
            "name": "BBB", "age": 1
        }, {
            "name": "CCC", "age": 1
        }
    ]
}
name = wangfeng["wifi"]["assistant"]["name"]
print(name)


#字段的删除  RuntimeError: dictionary changed size during
# iteration RuntimeError：迭代期间字典更改了大小
tem = []
dic = {
    "盖伦": "蹲草大宝剑",
    "皇子": "能击飞盖人",
    "亚索": "eeeeeeee",
    "蛮子": "五秒真男人",
}
for key in dic:
    if key.startswith("盖"):
        # dic.pop(key)
        tem.append(key)
for key in tem:
    dic.pop(key)
print(dic)

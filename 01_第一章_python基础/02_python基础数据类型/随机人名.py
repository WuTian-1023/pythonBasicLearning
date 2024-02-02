import random

# 定义姓氏和名字的列表
first_names = ['张', '李', '王', '刘', '陈', '杨', '赵', '黄', '周', '吴']
last_names = ['伟', '芳', '娜', '敏', '静', '丽', '强', '磊', '洋', '艳']

for i in range(10):
    # 随机选择一个姓氏和名字
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # 组合成完整的名字
    full_name = first_name + last_name
    print(full_name)


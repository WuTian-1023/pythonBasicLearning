# 我叫xxx
# name = input("请输入你的名字：")
# address = input("请输入你的住址：")
# age = int(input("请输入你的年龄："))
# hobby = input("请输入你的爱好：")

# %s 字符串占位 %d 占位数字

# s = "我叫%s,我住在%s，我今年%d岁，我喜欢做%s" % (name, address, age, hobby)
# print(s)
# s1 = "我叫{},我住在{}，我今年{}岁，我喜欢做{}".format(name, address, age, hobby)
# print(s1)
# f-string
# s2 = f"我叫{name},我住在{address}，我今年{age}岁，我喜欢做{hobby}"
# print(s2)

# 索引和切片
# 索引：按照位置来提取元素
# s = "我叫周杰伦"
# print(s[3])
# print(s[-1]) #-代表倒数

# 切片：从一个字符串中提取一部分
# str = "我叫周杰伦，你呢？你是蔡徐坤吗？"
# print(str[3:-2])
# print(str[:-2]) #start 如果是 从0开始 ,可以省略
# print(str[0:]) # 从start 开始 一直到结尾

# print(str[-3:-2]) 只能从左往右切
# print(str[-1:-3]) 没有结果
# s = "我爱你"
# 可以给切片添加步长来控制切片的方向
# print(s[::-1]) #- 表示从右往左
# 语法 s[start:end:step] 从start 到 end 每step个元素出来一个元素
# s ="asdfghjklqwertyuiop"
# print(s[-1:-8:-2])

# 字符串的常规操作
# 字符串的操作 一般不会对原来的字符串产生影响 一般返回一个新的字符串
# s = "python"
# 首字母大写
# s1 = s.capitalize()
# print(s1)

# 单词首字母大写
# s = "I have a dream!"
# s1 = s.title()
# print(s1)

# 切换小写
# s = "I HAVE A DREAM"
# s1 = s.lower()
# print(s1)
#
# s = "i have a dream"
# s1 = s.upper()
# print(s1)
#
# # 如何忽略大小写来进行判断
# verify_code = "xAt1"
# user_input = input(f"请输入验证码({verify_code})")
# if user_input.upper() == verify_code.upper():
#     print("验证码校验通过")
# else:
#     print("验证码输入有误")

# 3.2 字符串的切割和替换
# strip() 去掉字符串左右两边的空白符 空格 \t \n
# s = "    你好,     我叫   周杰伦    "
# s1 = s.strip()
# print(s1)
#
#
# username = input("请输入用户名")
# password = input("请输入密码")
# if username.strip() == "admin":
#     if password.strip() == "123456":
#         print("登录成功")
#     else:
#         print("登录失败")
# else:
#     print("失败")


# 我 今天 特别高兴
# replace(old, new) 字符串替换
# s = "你好我叫赛丽亚~"
# s1 = s.replace("赛丽亚","周杰伦")
# print(s1)
#
# a = "hello i am a good man!"
# a1 = a.title().replace(" ","")
# print(a1)

# split 用什么切割就会损失掉谁 字符串切割
# a = "python_java_c_c#_javascript"
# lst = a.split("_")
# print(lst)

# replace split strip  替换 切割 去空字符

# 3.4 查找与替换
s = "你好,我叫周润发"
# ret = s.find("周润发")
# print(ret) 返回出现的位置 -1代表没找到
# ret.s.index("周润发") #如果没有就报错
# print("周润发" in s) #存在返回 true 不存在返回 false ,in 可以做条件上的判断
# print("周润发" not in s)
# for c in s:
#     print(c)

# 判断
# name = input("请输入你的名字")
# if name.startswith("张"):
#     print("你姓张")
# else:
#     print("不姓张")
#

# 判断用户输入的是不是数字
# money = input("请输入你兜里的钱")
# if money.isdigit():
#     money = int(money)
#     print("可以花钱了")
# else:
#     print("对不起，您输入有误。。。")

s = "hello"

print(len(s))  #len() 返回字符串的长度

lst = ["赵本山","王大拿","大张伟","马大哈"]
s = "_".join(lst)
print(s)

# 总结
# 1.f"{变量}" 格式化一个字符串
# 2.索引和切片
#     索引: 从0开始的[]
    # 切片: s[start, end,step]  end位置的数据永远拿不到
# 3.字符串操作对元字符串是不发生改变的
#     1.upper() 在需要忽略大小写的时候使用
#     2.strip() 可以去掉字符串左右两端的空白
    # 3.replace() 字符串替换
    # 4.split() 对字符串进行切割
    # 5.join() 拼接一个列表中的内容 成为新的字符串
    # 7.len() 字符串的长度
    # 字符串的循环和遍历
    # for c in s:
           # print(c) 字符串中的每一个字符

    # 关于in:
        # 判断xxx是否在xxxx中出现了
        
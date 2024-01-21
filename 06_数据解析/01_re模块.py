import re

findall = re.findall("a", "abcabcabc")
print(findall)

findall = re.findall(r"\d+", "我今年18岁，电话号码是13574412345")
print(findall)

for item in findall:
    print(item)

# search
search = re.search(r"\d+", "我今年18岁，电话号码是13574412345")
print(search.group()) # 只会匹配第一次匹配的内容

# match
match = re.match(r"\d+", "我今年18岁，电话号码是13574412345")
print(match) # 只会匹配开头的内容 所以结果是 None

# 预加载 提前把正则表达式编译好
re_compile = re.compile(r"\d+")
compile_findall = re_compile.findall("我今年18岁，电话号码是13574412345")
print(compile_findall)


# 想要提取数据必须用()括起来,可以单独起名字
# (?P<name>正则表达式)
# 提取数据的时候 需要group("name")来提取
s = """
<div class='animal'><spen id='DXX'>大猩猩</spen></div>
<div class='animal'><spen id='DXM'>大熊猫</spen></div>
<div class='animal'><spen id='JQB'>金钱豹</spen></div>
"""
pattern = re.compile(r"<spen id='(?P<id>.*?)'>(?P<name>.*?)</spen>")
pattern_findall = pattern.finditer(s)
for item in pattern_findall:
    print(item.group("id"))
    print(item.group("name"))

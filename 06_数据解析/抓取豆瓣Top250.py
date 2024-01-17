"""
抓取豆瓣Top250电影数据
    1.确定url地址
    2.发请求获取页面数据
    3.解析数据
    4.保存数据
"""
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
# 1.确定url地址
url = "https://movie.douban.com/top250"
# 2.发请求获取页面数据 代理
proxies = {
  "http": "http://8.213.128.90:8080",
  "https": "http://8.213.128.90:8080",
}
requests_get = requests.get(url, headers=headers)
print(requests_get.text)
# 编写正则表达式
pattern = re.compile(r'<div class="item">'
                     r'.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<p class="">.*?导演: (?P<daoYan>.*?)&nbsp;.*?<br>'
                     r'(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">'
                     r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)</span>'
                     , re.S)  # re.S表示可以匹配换行符
# 3.解析数据
pattern_findall = pattern.finditer(requests_get.text)
for item in pattern_findall:
    name = item.group("name")
    daoYan = item.group("daoYan")
    year = item.group("year").strip()  # 去除空格
    score = item.group("score")
    num = item.group("num")
    # 4.保存数据
    with open("豆瓣Top250电影前25.csv", "a", encoding="utf-8") as f: # a表示追加
        f.write(f"{name},{daoYan},{year},{score},{num}\n")

f.close() # 关闭文件
requests_get.close() # 关闭请求
print("保存成功")

# 目前只获取到了第一页的数据，如何获取其他页的数据呢？
# 1.确定url地址
url = "https://movie.douban.com/top250?start="
index = 0
for i in range(10):
    # 2.发请求获取页面数据
    requests_get = requests.get(url=url + str(index), headers=headers)
    index += 25
    # 3.解析数据
    pattern_findall = pattern.finditer(requests_get.text)
    # 4.保存数据
    for item in pattern_findall:
        name = item.group("name")
        daoYan = item.group("daoYan")
        year = item.group("year").strip()  # 去除空格
        score = item.group("score")
        num = item.group("num")
        # 4.保存数据
        with open("豆瓣Top250电影.csv", "a", encoding="utf-8") as f: # a表示追加
            f.write(f"{name},{daoYan},{year},{score},{num}\n")

# 5.关闭文件和请求
f.close() # 关闭文件
requests_get.close() # 关闭请求
# 6.提示保存成功
print("保存成功")


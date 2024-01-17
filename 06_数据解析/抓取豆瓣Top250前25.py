"""
抓取豆瓣Top250电影数据
    1.确定url地址
    2.发请求获取页面数据
    3.解析数据
    4.保存数据
"""
import time

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
text = requests_get.text
if text.find("有异常请求从你的 IP 发出") != -1:
    print("触发反爬机制了！")
    exit()
# 编写正则表达式
pattern = re.compile(r'<div class="item">.*?<span class="title">(?P<title>.*?)'
                     r'</span>.*?<p class="">.*?导演: (?P<director>.*?)(?:\.\.\.|&nbsp;)'
                     r'.*?(?P<year>\d{4})&nbsp;'
                     r'.*?<span class="rating_num" property="v:average">(?P<score>\d\.\d)</span>'
                     r'.*?<span>(?P<reviews>\d+)人评价</span>'
                     , re.S)  # re.S表示可以匹配换行符

# pattern = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<title>.*?)</span>'
#                      r'.*?<p class="">.*?导演: (?P<director>.*?)(?:\.\.\.|&nbsp;)'
#                      r'.*?(?P<year>\d{4})&nbsp;'
#                      r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
#                      r'.*?<span>(?P<reviews>.*?)人评价</span>', re.S)

# 3.解析数据
pattern_findall = pattern.finditer(requests_get.text)
for item in pattern_findall:
    name = item.group("title")
    daoYan = item.group("director")  # 导演和演员  导演: (?P<daoYan>.*?)(?:<br>|&nbsp;) byd有一部剧导演后面没有&nbsp;
    year = item.group("year").strip()  # 去除空格
    score = item.group("score")
    num = item.group("reviews")
    # 4.保存数据
    with open("豆瓣Top250电影前25.csv", "a", encoding="utf-8") as f:  # a表示追加
        f.write(f"{name},{daoYan},{year},{score},{num}\n")

f.close()  # 关闭文件
requests_get.close()  # 关闭请求
print("保存成功")

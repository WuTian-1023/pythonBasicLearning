"""
https://dy2018.com/
1.提取到主页面中每个电影背后的链接
    1.拿到"2024必看热片"
2.访问子页面，提取到电影的下载链接和名称
"""

import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

url = "https://dy2018.com"

requests_get = requests.get(url, headers=headers)
requests_get.encoding = "gbk"
text = requests_get.text

# 提取2024必看热片
re_compile = re.compile(r"2024必看热片.*?<ul>(?P<html>.*?)</ul>", re.S)
iterator = re_compile.search(text)
html = iterator.group("html")

# 提取 <a href='/i/92364.html 中的href
re_compile2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)  # re.S表示可以匹配换行符  <a href='(?P<href>.*?)' .*?表示非贪婪模式
iterator2 = re_compile2.finditer(html)

re_compile3 = re.compile(r'.*?◎片　　名(?P<Name>.*?)<br />'
                         r'.*?◎年　　代(?P<Year>.*?)<br />'
                         r'.*?◎产　　地(?P<Place>.*?)<br />'
                         r'.*?◎类　　别(?P<Category>.*?)<br />'
                         r'.*?◎语　　言(?P<Language>.*?)<br />'
                         r'.*?◎字　　幕(?P<Subtitle>.*?)<br />'
                         r'.*?◎上映日期(?P<ReleaseDate>.*?)<br />'
                         r'.*?◎豆瓣评分(?P<Score>.*?)<br />'
                         r'.*?◎简　　介(?P<Introduction>.*?)<br />'
                         r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<DownloadLink>.*?)">.*?'
                         , re.S)  # 把子页面的正则表达式在for外面创建

for item in iterator2:
    href = item.group("href")
    #     拼接url 去访问详情
    detail_url = url + href
    print("请求的详情页 url：", detail_url)
    # 访问详情页
    detail_html = requests.get(detail_url, headers=headers)
    detail_html.encoding = "gbk"
    detail_text = detail_html.text
    if detail_text.find("404错误") != -1:
        print("404错误")
        continue
    detail_search = re_compile3.search(detail_text)
    name = detail_search.group("Name")
    year = detail_search.group("Year")
    place = detail_search.group("Place")
    category = detail_search.group("Category")
    language = detail_search.group("Language")
    subtitle = detail_search.group("Subtitle")
    release_date = detail_search.group("ReleaseDate")
    score = detail_search.group("Score")
    introduction = detail_search.group("Introduction")
    download_link = detail_search.group("DownloadLink")
    print(name, year, place, category, language, subtitle, release_date, score, introduction,
          download_link)
    #     保存数据
    with open("file/text/电影天堂.csv", "a", encoding="utf-8") as f:
        f.write(
            f"{name},{year},{place},{category},{language},{subtitle},{release_date},{score},{introduction},{download_link}\n")

# 关闭文件和请求
detail_html.close()
requests_get.close()
f.close()
print("保存成功")

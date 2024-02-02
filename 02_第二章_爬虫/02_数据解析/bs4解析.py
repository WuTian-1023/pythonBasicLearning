# 安装bs4
from bs4 import BeautifulSoup

html = """
<ul>
    <li><a href="zhangwuji.com">张无忌</a></li>
    <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
    <li><a href="zhangcuishan.com">张翠山</a></li>
    <li><a href="zhangcuishan.com">张翠山</a></li>
    <a href="jingmaoshiwang.com">金毛狮王</a>
</ul>
"""

page = BeautifulSoup(html, "html.parser")
# page.find("标签名", attrs={"属性":"值"}) #找某个元素

# page.find_all("标签名", attrs={"属性":"值"}) # 找一堆

li = page.find("li", attrs={"id": "abc"})
print(li)
print(li.find("a"))
print(li.find("a").text)
print(li.find("a").get("href"))

all_li = page.find_all("li")
for li in all_li:
    a = li.find("a")
    href = a.get("href")
    text = a.text
    print(href, text)

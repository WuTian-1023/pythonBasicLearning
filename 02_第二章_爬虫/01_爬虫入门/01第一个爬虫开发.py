from urllib.request import urlopen

url = "http://www.baidu.com"

resp = urlopen(url)
# print(resp.read().decode("utf-8")) # 此时拿到的是页面源代码 这里打印后 下面的文件就没有了

with open("baidu.html", mode="w", encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))

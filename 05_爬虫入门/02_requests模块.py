import requests

url = "http://wwww.baidu.com"

get = requests.get(url)
get.encoding = "utf-8"
print(get)
print(get.text) # 拿到页面源代码

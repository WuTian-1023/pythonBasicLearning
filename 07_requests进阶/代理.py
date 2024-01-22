import requests
"""
免费的代理 https://www.kuaidaili.com/free/inha/
"""
url = "https://www.baidu.com"

# 准备代理信息
proxy = {
    "http": "http://180.120.179.126:11343",
    "https": "https://180.120.179.126:11343"
}

# 发请求
requests_get = requests.get(url=url, proxies=proxy, timeout=10)
requests_get.encoding = "utf-8"
print(requests_get.text)
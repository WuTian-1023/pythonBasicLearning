import requests

content = input('请输入你要搜索的内容：')
url = "https://movie.douban.com/j/chart/top_list"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

data = {
    "type": "13",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}
# get请求
# 处理一个简单的反爬机制
requests_get = requests.get(url, headers=headers, params=data)
print(requests_get.json())

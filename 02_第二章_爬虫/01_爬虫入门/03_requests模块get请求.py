import requests

content = input('请输入你要搜索的内容：')
url = f"https://www.sogou.com/web?query={content}"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

proxies = {
  "http": "http://58.20.248.139:9002",
  "https": "http://58.20.248.139:9002",
}
# get请求
# 处理一个简单的反爬机制
requests_get = requests.get(url, headers=headers, proxies=proxies)
print(requests_get.text)

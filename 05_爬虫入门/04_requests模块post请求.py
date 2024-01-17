import requests

url = "https://fanyi.baidu.com/sug"

fromdata = {
    "kw":input("单词：")
}

requests_post = requests.post(url, data=fromdata)
print(requests_post.json()) # 拿到的是json格式的数据

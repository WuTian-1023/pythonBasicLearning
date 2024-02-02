"""
    登录 -> 获取个人信息得到cookie
    带着cookie 去请求书架

    必须得把上面的两个请求放在一个session里面
    我们可以使用session进行请求 -> session 你可以认为是一连串的请求
"""

import requests

# 会话
session = requests.session()

# 登录
data = {
    "loginName": "你的loginName",
    "password": "你的password"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

loginUrl = 'https://passport.17k.com/ck/user/login'
session_get = session.post(url=loginUrl, data=data, headers=headers)
# print(session_get.text)

# 获取书架的数据
response = session.get(url='https://user.17k.com/ck/user/myInfo/102947196?bindInfo=1&appKey=2406394919')
response.encoding = "utf-8"
print(response.json())
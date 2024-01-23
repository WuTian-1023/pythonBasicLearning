"""
确定url https://www.acfun.cn/u/56776847

"""
import os
import time

import requests
import re
from lxml import etree  # xpath解析库
from 实战_a站视频 import main

# 1.确定url地址
url = "https://www.acfun.cn/u/56776847"
# 详情页前缀   /v/ac43577708 ->  https://www.acfun.cn/v/ac43560414
prefix_url = "https://www.acfun.cn"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
def create_directory(directory_path):
    try:
        # 如果目录不存在，则创建它
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"目录 '{directory_path}' 已创建。")
        else:
            print(f"目录 '{directory_path}' 已存在。")
    except Exception as e:
        print(f"创建目录时发生错误: {e}")
# 把所有的视频的url地址放到一个列表中
all_video_url = []
# 2.发请求获取页面数据
requests_get = requests.get(url=url, headers=headers)
requests_get.encoding = "utf-8"
html = requests_get.text
# print(html)
# 3.解析数据
# 先找up主的名字 和 视频数量 以及视频的url地址
etree_html = etree.HTML(html)
# 视频总数量
num = etree_html.xpath("//li[@class='active']/span/text()")[0]
# up主的名字
name = etree_html.xpath("//span[@class='text-overflow name']/text()")[0]
print(f"up主的名字：{name}，视频总数量：{num}")

# 找视频的url地址
hrefs = etree_html.xpath("//div[@id='ac-space-video-list']/a/@href")
# 先装第一页的视频url地址
all_video_url = [prefix_url + href for href in hrefs]
# 找到下一页的url地址 根据num判断页数 一页20个视频
# 页数
page = int(num) // 20 + 1
# 下一页的url地址
for i in range(2, page + 1): # 从第二页开始 因为第一页已经装了
    # 获取当前时间戳
    current_timestamp = time.time()
    next_url = url + f"?quickViewId=ac-space-video-list&reqID={i}&ajaxpipe=1&type=video&order=newest&page={i}&pageSize=20&t={current_timestamp}"
    print(next_url)
    # 发请求获取页面数据
    requests_get = requests.get(url=next_url, headers=headers)
    requests_get.encoding = "utf-8"
    html = requests_get.text
    # 解析数据 使用正则
    """
    这段代码使用了正则表达式href="([^"]+)"，其中：
    
    href="：匹配字面字符串href="。
    ([^"]+)：匹配并捕获一次或多次不是引号"的任意字符。[^"]表示匹配除了双引号以外的任意字符，+表示匹配前面的子表达式一次或多次。
    "：字面上匹配一个双引号，表示href属性值的结束。
    matches.group(1)返回第一个括号中匹配的文本，即href属性的值。
    
    这个正则表达式假设href的值不包含双引号
    """
    hrefs = re.findall(r'href=\\"(.*?)"', html, re.S)
    for href in hrefs:
        # href /v/ac42368063\\ 去 \\
        href = href.replace("\\", "")
        all_video_url.append(prefix_url + href)

all_video_url = list(set(all_video_url))  # 去重

# 创建目录
create_directory(f"./file/video/{name}")

# 下载
for item in all_video_url:   # 传入的是视频的url地址
    main(item, name)

print("所有视频下载完成")






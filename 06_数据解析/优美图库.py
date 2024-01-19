"""
https://www.youmeitu.com/meinv/  # 不爬这个 这个不好看
咱们爬这个: https://www.umei.net/ # 这个好看 https://www.umei.net/  + tupian/68660.html
"""
from bs4 import BeautifulSoup
import requests
import os


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


# 1. 确定url
url = "https://www.umei.net/i/index_5.html"
# https://www.umei.net/i/index_2.html 这是第二页的路径

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# 2. 发请求
index = requests.get(url=url, headers=headers)
index.encoding = "utf-8"
index_html = index.text
# print(index_html)
page = BeautifulSoup(index_html, "html.parser")
find_all = page.find_all("li", attrs={"class": "i_list list_n2"})
for item in find_all:
    href = item.find("a").get("href")  # 获取到了每个图片的详情页的url
    title = item.find("a").get("title")  # 获取标题用来创建文件夹
    #   拼接详情url
    detail_url = url + href
    print(f"请求的地址:{detail_url}和标题:{title}")
    num = 1  # 计数
    while True:
        detail_html = requests.get(url=detail_url, headers=headers)
        detail_html.encoding = "utf-8"
        detail_html_text = detail_html.text
        #     好问题又来了 图片要翻页获取所有
        ret = BeautifulSoup(detail_html_text, "html.parser")
        div = ret.find("div", attrs={"class": "image_div"})
        # 获取下一页的地址
        next_page = div.find("a").get("href")
        next_url = url + next_page
        if next_page == "/tupian/":
            print(f"没有下一页了,已经下完了!标题:{title}")
            num = 1  # 重置num
            break
        else:
            detail_url = next_url
            download_url = div.find("img").get("src")  # 获取图片下载的url 只在有图片的页面才有
            print(f"图片的url:{download_url}, 下一页的地址:{next_url}")
            # 下载图片
            img = requests.get(url=download_url, headers=headers)
            create_directory(f"./file/image/{title}")  # 创建文件夹
            with open(f"./file/image/{title}/{title}_{num}.jpg", "wb") as f:
                f.write(img.content)  # 保存图片
            num += 1
            print(f"{title}的第{num}张图片下载完成!")
    #break # 测试只爬一个 放开的话就是爬所有

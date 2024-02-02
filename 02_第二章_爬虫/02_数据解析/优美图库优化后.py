from bs4 import BeautifulSoup
import requests
import os
import threading
import time


def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"目录 '{directory_path}' 已创建。")
    else:
        print(f"目录 '{directory_path}' 已存在。")


def download_image(session, download_url, directory_path, title, num):
    create_directory(directory_path)  # 确保目录已创建
    image_path = f"{directory_path}/{title}_{num}.jpg"
    if not os.path.exists(image_path):
        try:
            img = session.get(url=download_url, headers=headers, timeout=10)
            if img.status_code == 200:
                with open(image_path, "wb") as f:
                    f.write(img.content)  # 保存图片
                print(f"{title}的第{num}张图片下载完成!")
            else:
                print(f"下载失败: {download_url}, 状态码: {img.status_code}")
        except requests.RequestException as e:
            print(f"下载时发生错误: {e}")
    else:
        print(f"{title}的第{num}张图片已存在。")


# 使用Session进行网络请求
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
session.headers = headers

# 1. 确定url
url = "https://www.umei.net/i/index_2.html"
csUrl = "https://www.umei.net"

# 2. 发请求
index = session.get(url=url)
index.encoding = "utf-8"
index_html = index.text

# 解析页面
page = BeautifulSoup(index_html, "html.parser")
find_all = page.find_all("li", attrs={"class": "i_list list_n2"})

for item in find_all:
    href = item.find("a").get("href")  # 获取到了每个图片的详情页的url
    title = item.find("a").get("title")  # 获取标题用来创建文件夹
    detail_url = csUrl + href
    print(f"请求的地址:{detail_url}和标题:{title}")

    num = 1  # 计数
    threads = []  # 线程列表
    while True:
        time.sleep(1)  # 在请求详情页面之前增加延时
        detail_html = session.get(url=detail_url)
        detail_html.encoding = "utf-8"
        ret = BeautifulSoup(detail_html.text, "html.parser")
        div = ret.find("div", attrs={"class": "image_div"})
        next_page = div.find("a").get("href")
        next_url = csUrl + next_page

        if next_page == "/tupian/":
            print(f"没有下一页了,已经下完了!标题:{title}")
            num = 1  # 重置num
            break
        else:
            detail_url = next_url
            download_url = div.find("img").get("src")

            # 创建并启动线程
            thread = threading.Thread(target=download_image,
                                      args=(session, download_url, f"./file/image/{title}", title, num))
            threads.append(thread)
            thread.start()

            num += 1

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    time.sleep(1)  # 每次完成一组图片下载后暂停1秒
# 如果要爬取多页，可以将上述逻辑放入一个循环中，并更新url变量为下一页的地址

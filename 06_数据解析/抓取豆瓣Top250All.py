"""
抓取豆瓣Top250电影数据
    1.确定url地址
    2.发请求获取页面数据
    3.解析数据
    4.保存数据
"""
import time
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
# 发请求获取页面数据 代理
proxies = {
    "http": "http://8.213.128.90:8080",
    "https": "http://8.213.128.90:8080",
}


# 检查是否触发反爬机制
def checkAntiSpider(text):
    if text.find("有异常请求从你的 IP 发出") != -1:
        print("触发反爬机制了！")
        exit()


# 编写正则表达式
# 封装一下
def getPattern():
    pattern = re.compile(r'<div class="item">.*?<span class="title">(?P<title>.*?)'
                         r'</span>.*?<p class="">.*?导演: (?P<director>.*?)(?:\.\.\.|&nbsp;)'
                         r'.*?(?P<year>\d{4})&nbsp;'
                         r'.*?<span class="rating_num" property="v:average">(?P<score>\d\.\d)</span>'
                         r'.*?<span>(?P<reviews>\d+)人评价</span>'
                         , re.S)  # re.S表示可以匹配换行符
    return pattern


# 目前只获取到了第一页的数据，如何获取其他页的数据呢？--已解决
# 新的问题：反爬虫机制，如何解决？多线程？？
# 1.确定url地址
url = "https://movie.douban.com/top250?start="
index = 0  # 从0开始
total = 0  # 总共保存了多少条数据


def main():  # 定义一个main函数
    pattern = getPattern()  # 调用getPattern函数 放在循环外面 优化代码避免每次都调用
    global index, total  # 声明index和total是全局变量
    for i in range(10):
        time.sleep(3)  # 为了防止被封IP
        # 2.发请求获取页面数据
        requests_get = requests.get(url=url + str(index), headers=headers)
        checkAntiSpider(requests_get.text)  # 检查是否触发反爬机制
        index += 25  # 每次加25
        # 3.解析数据
        pattern_findall = pattern.finditer(requests_get.text)
        # 延迟3秒
        time.sleep(3)  # 为了防止被封IP
        # 4.保存数据
        for item in pattern_findall:
            name = item.group("title")
            daoYan = item.group("director")
            year = item.group("year").strip()  # 去除空格
            score = item.group("score")
            num = item.group("reviews")
            print(f"{name},{daoYan},{year},{score},{num} --第多少 {total} 条")
            # 4.保存数据
            with open("file/text/豆瓣Top250电影.csv", "a", encoding="utf-8") as f:  # a表示追加
                f.write(f"{name},{daoYan},{year},{score},{num}\n")
            total += 1
        print(f"第{i + 1}页保存成功 保存了{total}条数据")
        #     延迟3秒
        time.sleep(3)  # 为了防止被封IP

    # 5.关闭文件和请求
    f.close()  # 关闭文件
    requests_get.close()  # 关闭请求
    # 6.提示保存成功
    print("保存成功")


#  7.调用main函数
if __name__ == '__main__':
    main()  # 调用main函数

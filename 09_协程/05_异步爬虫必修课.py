# aiofiles 是一个异步文件操作库，asyncio 是 Python3.4 之后内置的异步 IO 框架
# aiohttp 是一个异步请求库，asyncio 是 Python3.4 之后内置的异步 IO 框架
# aiohttp 可以与 asyncio 配合使用，实现异步请求
# aiohttp 的使用步骤：
#     1. 创建一个异步请求对象
#     2. 发起请求
#     3. 获取响应数据
#     4. 关闭请求对象
#     5. 关闭事件循环
import asyncio
import time

import aiohttp
import aiofiles
import os
from multiprocessing import Process
import requests
from lxml import etree  # xpath解析库

# 前缀
prefix_url = "https://www.qqtn.com/"
# 列表url 每个页面有多个列表 点击进去有详情页 我们要下载详情页的图片
list_url = "https://www.qqtn.com/tp/sgtp_1.html"
# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


# 获取列表页数据
def get_list_data(url):
    response = requests.get(url, headers=headers)
    response.encoding = "gb2312"
    return response.text


# 解析list页面获取到详情url列表
def parse_list_data(html):
    tree = etree.HTML(html)
    detail_urls = tree.xpath('//ul[@class="g-gxlist-imgbox"]/li/a/@href')
    return detail_urls


# 获取详情页数据
def get_detail_data(detail_url):
    prefix_url + detail_url
    response = requests.get(prefix_url + detail_url, headers=headers)
    response.encoding = "gb2312"
    return response.text


# 解析详情页数据获取图片url列表
def parse_detail_data(html):
    tree = etree.HTML(html)
    title = tree.xpath('//div[@class="g-cont-detail g-main-bg"]/h1/text()')[0]  # 只有一个标题
    img_urls = tree.xpath('//div[@class="m_qmview"]/p/img/@src')
    return title, img_urls


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


# 保存图片
async def save_data(title, img_urls):
    # 创建目录
    create_directory(f"./file/image/{title}")
    for img_url in img_urls:
        # 创建异步请求对象
        async with aiohttp.ClientSession() as session:  # async with 用于创建一个异步请求对象
            # 发起请求
            async with session.get(img_url, headers=headers) as response:  # 这里的response是一个响应对象 不能直接获取响应数据 需要调用read()方法
                # 获取响应数据
                img_data = await response.read()  # await 用于挂起当前协程，等待异步操作完成，获取异步操作的结果
                # 保存图片
                async with aiofiles.open(f"./file/image/{title}/{img_url[-10:]}", mode="wb") as f:
                    await f.write(img_data)
                    print(f"{img_url} 保存成功")


def main():
    # 获取列表页HTML
    list_html = get_list_data(list_url)
    # 解析列表页获取详情页URLs
    detail_urls = parse_list_data(list_html)

    processes = []

    for detail_url in detail_urls:
        # 对每个详情页创建一个进程
        process = Process(target=process_detail_page, args=(detail_url,))
        processes.append(process)
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()
    # 关闭资源
    for process in processes:
        process.close()


def process_detail_page(detail_url):
    # 获取详情页数据
    detail_html = get_detail_data(detail_url)
    # 解析详情页数据获取图片url列表
    title, img_urls = parse_detail_data(detail_html)
    # 创建目录并保存图片 保存图片的操作是异步的
    asyncio.run(save_data(title, img_urls))


if __name__ == '__main__':
    # 计时
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"耗时：{end_time - start_time}")
    # 异步保存耗时：7.585883140563965 对比 同步保存耗时：18.70596742630005 速度提升了一倍多 但是还是慢 有待优化

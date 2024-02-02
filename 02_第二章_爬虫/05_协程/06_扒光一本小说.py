import time
from multiprocessing import Process

import aiohttp
import requests
import asyncio
import hashlib
import aiofiles
import os
import re
from lxml import etree  # xpath解析库
from tqdm import tqdm

"""
https://www.biquge635.com/
https://www.biquge635.com/book/40420/
"""

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


def get_list_data(url):
    response = requests.get(url, headers=headers)
    response.encoding = "gbk"
    text = response.text
    # print(text)
    return text


# 解析页面数据 获取每一章节的url地址 以及章节的名字 再取一下书名
def analysis_list_data(html):
    tree = etree.HTML(html)
    # 书名
    book_name = tree.xpath('//div[@class="top"]/h1/text()')[0]
    # print(book_name)
    # 章节url地址
    chapter_urls = tree.xpath('//div[@class="section-box"]/ul/li/a/@href')
    # print(chapter_urls)
    # 章节名字
    chapter_names = tree.xpath('//div[@class="section-box"]/ul/li/a/text()')
    # print(chapter_names)
    return book_name, chapter_urls, chapter_names


# 访问详情页 获取详情页的数据
# async def get_detail_data(url):
#     response = requests.get(url, headers=headers)
#     response.encoding = "gbk"
#     text = response.text
#     # print(text)
#     return text

# async def get_detail_data(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, headers=headers) as response:
#             response.encoding = 'gbk'
#             return await response.text()  # 下载或保存 第1492章 窃福 时出错: 'utf-8' codec can't decode byte 0xb5 in position 439: invalid start byte


# async def get_detail_data(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, headers=headers) as response:
#             # 读取原始字节数据
#             raw_data = await response.read()
#             # 将GBK编码的字节数据转换为字符串
#             return raw_data.decode('gbk')

# 重试机制
# async def get_detail_data(url, retry=3):
#     async with aiohttp.ClientSession() as session:
#         try:
#             async with session.get(url, headers=headers, timeout=10) as response: # 设置超时时间 10s
#                 # 读取原始字节数据
#                 raw_data = await response.read()
#                 # 将GBK编码的字节数据转换为字符串
#                 return raw_data.decode('gbk')
#         except Exception as e:
#             if retry > 0:
#                 print(f"请求出错，正在重试... 剩余重试次数: {retry}")
#                 return await get_detail_data(url, retry - 1)
#             else:
#                 raise

async def get_detail_data(url, session, retries=3):
    for attempt in range(retries):
        try:
            # 尝试发起GET请求
            async with session.get(url) as response:
                if response.status == 200:
                    # 请求成功，返回响应内容
                    return await response.read()
                else:
                    # 打印状态码非200的尝试信息
                    print(f"尝试 {attempt + 1} 失败，状态码：{response.status}")
        except aiohttp.ClientPayloadError as e:
            # 捕获并打印载入数据不完整的错误
            print(f"尝试 {attempt + 1} 失败，载入数据不完整：{e}")
            if attempt < retries - 1:
                # 如果不是最后一次尝试，等待后重试
                await asyncio.sleep(2 ** attempt)  # 指数退避
            else:
                # 最后一次尝试失败后，重新抛出异常
                raise


# 解析详情页数据 获取每一章节的内容
def analysis_detail_data(html):
    tree = etree.HTML(html)
    # 章节内容
    chapter_content = tree.xpath('//div[@id="content"]/text()')
    # 还需要解析 去空格 去\xa0 去\xa0\xa0\xa0\xa0 去换行
    chapter_content = "\n".join(chapter_content).replace("\xa0\xa0\xa0\xa0", "")
    # print(chapter_content)
    return chapter_content


def create_directory(directory_path):
    try:
        # 如果目录不存在，则创建它
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"目录 '{directory_path}' 已创建。")
    except Exception as e:
        print(f"创建目录时发生错误: {e}")


# 保存数据
async def save_data(book_name, title, data):
    # 创建目录
    create_directory(book_name)
    # 保存数据
    file_path = f"./{book_name}/{title}.txt"
    # async with open(file_path, mode="w", encoding="utf-8") as f:
    """
    您在代码中遇到的错误 '_io.TextIOWrapper' object does not support the asynchronous context manager protocol 
    是因为您尝试使用 async with 语句来异步打开文件，但 open 函数并不支持异步上下文管理器。在 Python 中，
    标准的 open 函数是同步的，即使在异步函数中使用它也是如此。要异步地打开和操作文件，您需要使用 aiofiles 库。
    """
    async with aiofiles.open(file_path, mode="w", encoding="utf-8") as f:
        await f.write(data)
    print(f"{title}保存成功")


# 访问详情页 获取详情页的数据 保存

# async def download_detail_data(url, book_name, title):
#     print(url, book_name, title)
#     html = await get_detail_data(url)  # 使用 await 等待异步操作完成
#     data = analysis_detail_data(html)
#     await save_data(book_name, title, data)  # 使用 await 等待异步操作完成


# async def download_detail_data(url, book_name, title):
#     try:
#         print(url, book_name, title)
#         html = await get_detail_data(url)
#         data = analysis_detail_data(html)
#         if data:
#             await save_data(book_name, title, data)
#         else:
#             print(f"章节内容为空: {title}")
#     except Exception as e:
#         print(f"下载或保存 {title} 时遇到未知错误: {e}, URL: {url}")


async def download_detail_data(url, book_name, title, session):
    try:
        print(url, book_name, title)
        html = await get_detail_data(url, session)
        data = analysis_detail_data(html)
        if data:
            await save_data(book_name, title, data)
        else:
            print(f"章节内容为空: {title}")
    except Exception as e:
        print(f"下载或保存 {title} 时遇到未知错误: {e}, URL: {url}")


async def main(url):
    async with aiohttp.ClientSession() as session:
        # 1.拿到页面当中每一章节的url地址
        list_data = get_list_data(url)
        data = analysis_list_data(list_data)
        # 章节名
        book_name = data[0]
        chapter_urls = data[1]
        chapter_names = data[2]
        tasks = []
        for chapter_url, chapter_name in zip(chapter_urls, chapter_names):
            chapter_url = url + chapter_url
            task = asyncio.create_task(download_detail_data(chapter_url, book_name, chapter_name, session))
            tasks.append(task)
        await asyncio.wait(tasks)


if __name__ == '__main__':
    # 计时
    start_time = time.time()
    # url
    url = "https://www.biquge635.com/book/40420/"
    # 然后在某个异步上下文中调用 main 函数
    asyncio.run(main(url))
    end_time = time.time()
    print(f"耗时：{end_time - start_time}")  # 耗时：112.28960633277893

"""
总结： async with aiohttp.ClientSession() as session: 
# async with 用于创建一个异步请求对象 使用session发起请求可以保持会话状态
async 在方法前面 代表这个方法是一个异步方法
await 用于挂起当前协程，等待异步操作完成，获取异步操作的结果
asyncio.run() 用于运行一个异步函数
asyncio.wait() 用于等待一组异步任务完成
await asyncio.wait(tasks) 用于等待一组异步任务完成
"""
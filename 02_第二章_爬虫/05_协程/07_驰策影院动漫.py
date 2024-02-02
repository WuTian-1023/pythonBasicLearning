"""
http://www.gxychina.com/
http://www.gxychina.com/chi/69.html 凡人修仙传列表
http://www.gxychina.com/na/69-1-85.html 凡人修仙传第一章 1-85
ERROR: Could not find a version that satisfies the requirement aiotqdm (from versions: none)
ERROR: No matching distribution found for aiotqdm 找不到满足aiotqdm要求的版本（来自版本：none）错误：未找到aioqdm的匹配分发

"""
import aiofiles
import aiohttp
import asyncio
import requests
from lxml import etree
import os
import time
import pprint
import re
from tqdm import tqdm

# 域名
prefix_url = "http://www.gxychina.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


# 获取列表页数据
def get_list_data(url):
    requests_get = requests.get(url=url, headers=headers)
    requests_get.encoding = "UTF-8"
    return requests_get.text


# 解析数据
def parse_list_data(html):
    etree_html = etree.HTML(html)
    playUrls = etree_html.xpath("//ul[@class='myui-content__list sort-list clearfix']/li/a/@href")
    return playUrls


# 获取剧名
def get_name(html):
    etree_html = etree.HTML(html)
    name = etree_html.xpath("//h1[@class='title text-fff']/text()")
    return name


# 获取标题名
def getTitles(html):
    etree_html = etree.HTML(html)
    Titles = etree_html.xpath("//ul[@class='myui-content__list sort-list clearfix']/li/a/@title")
    return Titles


# 获取详情页
async def parse_detail_data(session, url):
    async with session.get(url) as response:
        response.encoding = "UTF-8"
        text = await response.text()
        # 获页面中的m3u8地址
        search = re.search(';var now="(.*?)";var', text)
        return search


# 访问ts文件url拿到文件保存
async def get_ts_data(session, url):
    async with session.get(url) as response:
        response.encoding = "UTF-8"
        ts_data = await response.text()  # 加上圆括号来调用方法
        #   文本处理 从，开始 到#E结束
        ts_urls = re.findall(',\n(.*?)\n#E', ts_data, re.S)
        return ts_urls


def create_directory(directory_path):
    try:
        # 如果目录不存在，则创建它
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"目录 '{directory_path}' 已创建。")
    except Exception as e:
        print(f"创建目录时发生错误: {e}")


# async def download_ts_file(session, ts_url, f, progress):
#     async with session.get(ts_url) as response:
#         response.encoding = "UTF-8"
#         ts_data = await response.content.read()
#         await f.write(ts_data)
#         progress.update(1) # 有问题保存的视频乱了

async def download_ts_file(session, ts_url, ts_sequence, buffer_dict):
    async with session.get(ts_url) as response:
        response.encoding = "UTF-8"
        ts_data = await response.content.read()
        buffer_dict[ts_sequence] = ts_data


# 下载ts文件
# async def download_ts_data(session, ts_urls, name, title):
#     path_name = name[0].strip()
#     # 创建目录
#     print(f"剧名：{path_name}, 集数：{title}")
#     create_directory(path_name)
#     # 保存数据
#     file_path = f"./{path_name}/{title}.mp4"
#     print("保存路径：", file_path,"开始下载 ts 文件")
#     async with aiofiles.open(file_path, mode="ab") as f: # 追加写入
#         for ts_url in tqdm(ts_urls):
#             # 访问tsurl 拿到视频，拼接所有
#             async with session.get(ts_url) as response:
#                 response.encoding = "UTF-8"
#                 ts_data = await response.content.read()
#                 await f.write(ts_data)

# async def download_ts_data(session, ts_urls, name, title):
#     path_name = name[0].strip()
#     create_directory(path_name)
#     file_path = f"./{path_name}/{title}.mp4"
#     print(f"ts_urls, {ts_urls}")
#
#     progress = tqdm(total=len(ts_urls))
#     async with aiofiles.open(file_path, mode="ab") as f:
#         tasks = [asyncio.create_task(download_ts_file(session, ts_url, f, progress)) for ts_url in ts_urls]
#         await asyncio.gather(*tasks)
#     progress.close()
#
#     print("所有下载任务已完成")

async def download_ts_data(session, ts_urls, name, title):
    path_name = name[0].strip()
    create_directory(path_name)
    file_path = f"./{path_name}/{title}.mp4"
    print("保存路径：", file_path, "开始下载 ts 文件")

    buffer_dict = {}
    async with aiofiles.open(file_path, mode="ab") as f:
        tasks = [asyncio.create_task(download_ts_file(session, ts_url, i, buffer_dict))
                 for i, ts_url in enumerate(ts_urls)]
        await asyncio.gather(*tasks)

        # 确保按正确的顺序写入文件
        for i in range(len(ts_urls)):
            await f.write(buffer_dict[i])

        print("所有下载任务已完成")


async def download_detail_data(session, url, title, name):
    detail_data = await parse_detail_data(session, url)
    m3u8 = detail_data.group(1)
    # https://new.1080pzy.co/20211029/Oil0h7pU/index.m3u8 这是详情页返回的m3u8地址
    # https://new.1080pzy.co/20211029/Oil0h7pU/1400kb/hls/index.m3u8 通过页面上关键字查找，发现ts文件来自这个接口
    # 处理获取ts的链接
    ts_url = m3u8.replace("index.m3u8", "1400kb/hls/index.m3u8")  # 这里的1400kb是固定的，不知道是什么意思 直接替换
    ts_data = await get_ts_data(session, ts_url)
    # 下载ts文件
    await download_ts_data(session, ts_data, name, title)


async def main(url):
    # 创建统一的session
    async with aiohttp.ClientSession() as session:
        # 获取列表页数据
        list_data = get_list_data(url)
        data = parse_list_data(list_data)
        name = get_name(list_data)
        titles = getTitles(list_data)
        tasks = []
        for url, title in zip(data, titles):
            play_url = prefix_url + url
            print(play_url)
            task = asyncio.create_task(download_detail_data(session, play_url, title, name))
            tasks.append(task)
            break  # 测试只下载一集
        await asyncio.wait(tasks)


if __name__ == '__main__':
    # 计时
    start_time = time.time()
    # url
    url = "http://www.gxychina.com/chi/69.html"
    # 然后在某个异步上下文中调用 main 函数
    asyncio.run(main(url))
    end_time = time.time()
    print(f"耗时：{end_time - start_time}")  # 60.40073251724243

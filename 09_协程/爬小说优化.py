import time

import aiohttp
import asyncio
import aiofiles
from lxml import etree
import os
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

import aiohttp
import asyncio

# 定义异步的 fetch 函数，包含重试逻辑
async def fetch(url, session, retries=3):
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

async def parse_list_page(url, session):
    html = await fetch(url, session)
    tree = etree.HTML(html)
    book_name = tree.xpath('//div[@class="top"]/h1/text()')[0]
    chapter_urls = tree.xpath('//div[@class="section-box"]/ul/li/a/@href')
    chapter_names = tree.xpath('//div[@class="section-box"]/ul/li/a/text()')
    return book_name, chapter_urls, chapter_names

async def fetch_and_save_chapter(url, book_name, chapter_name, session):
    html = await fetch(url, session)
    tree = etree.HTML(html)
    chapter_content = tree.xpath('//div[@id="content"]/text()')
    chapter_content = "\n".join(chapter_content).replace("\xa0\xa0\xa0\xa0", "\n")

    directory_path = f"./{book_name}"
    os.makedirs(directory_path, exist_ok=True)
    file_path = os.path.join(directory_path, f"{chapter_name}.txt")

    async with aiofiles.open(file_path, mode="w", encoding="utf-8") as f:
        await f.write(chapter_content)
    print(f"{chapter_name}保存成功")

async def main(url):
    async with aiohttp.ClientSession(headers=headers) as session:
        book_name, chapter_urls, chapter_names = await parse_list_page(url, session)
        tasks = []
        for chapter_url, chapter_name in zip(chapter_urls, chapter_names):
            full_url = os.path.join(url, chapter_url)
            tasks.append(fetch_and_save_chapter(full_url, book_name, chapter_name, session))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    # 计时
    start_time = time.time()
    url = "https://www.biquge635.com/book/40420/"
    asyncio.run(main(url))
    end_time = time.time()
    print(f"耗时：{end_time - start_time}")  # 耗时：76.5492959022522s chatgpt代码
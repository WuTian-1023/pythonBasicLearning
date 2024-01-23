"""
正常的视频：
    完整的视频数据 --> 直接下载
流媒体：
    视频数据 --> 分段 --> 每一段视频数据的url地址 --> 下载
    把完整的视频分成很多小段，每一段视频数据的url地址 ts文件
1. 通过分析网页源代码，找到视频的url地址
2. 通过requests模块发送请求，获取响应数据

3. 保存视频数据

进阶 ：获取一个up猪的所有视频
    https://www.acfun.cn/u/56776847?quickViewId=ac-space-video-list&reqID=2&ajaxpipe=1&type=video&order=newest&page=1&pageSize=20&t=1705985425289

"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import requests
import re
from lxml import etree  # xpath解析库
import pprint
import json
from tqdm import tqdm

# 1.确定url地址
url = "https://www.acfun.cn/v/ac43577708"
# 视频前缀     https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video
prefix_url = "https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


# 获取视频的url地址和标题
def getVideoInfoAndTitle(url):
    # 2.发请求获取页面数据
    requests_get = requests.get(url=url, headers=headers)
    requests_get.encoding = "utf-8"
    html = requests_get.text
    # 3.解析数据
    # 先找标题
    etree_html = etree.HTML(html)
    title = etree_html.xpath('//div[@class="video-description clearfix"]/h1/span/text()')[0]  # 只有一个标题 使用xpath来取

    # 去除标题中的特殊字符
    title = re.sub(r"[\/\\\:\*\?\"\<\>\|]", "", title)

    # 再找视频的url地址
    videoInfo = re.findall(r"window.pageInfo = window.videoInfo = (.*?);", html, re.S)[0]
    return videoInfo, title


# 解析页面数据
def parseData(videoInfo):
    # 数据转json
    ksPlayJson = json.loads(videoInfo)['currentVideoInfo']['ksPlayJson']
    representation = json.loads(ksPlayJson)['adaptationSet'][0]['representation']
    backupUrl = representation[0]['backupUrl'][0]  # 视频的url地址

    # 发送请求获取视频数据
    m3u8_data = requests.get(url=backupUrl, headers=headers)
    m3u8_data.encoding = "utf-8"
    data_text = m3u8_data.text
    # 使用正则表达式获取视频的url地址
    findall = re.findall(r",\n(.*?)\n#E", data_text, re.S)
    return findall


# 下载视频
def downloadVideo(findall, title, name):
    for item in tqdm(findall):
        # 拼接视频的url地址
        m3u8_download_url = prefix_url + item
        print(m3u8_download_url)
        # 下载视频数据
        video_get = requests.get(url=m3u8_download_url, headers=headers)
        if video_get.status_code != 200:
            pprint.pprint(f"{title}.mp4下载失败,丢失片段：{m3u8_download_url},状态码：{video_get.status_code}")
            continue
        else:
            video = video_get.content
            with open(f"file/video/{name}/{title}.mp4", "ab") as f:
                f.write(video)
            print(f"下载完成 {title}.mp4")
            f.close()


def download_segment(args):
    """下载单个视频片段并保存到临时文件"""
    index, m3u8_download_url, name, title = args
    temp_filename = f"temp_{index:05d}.ts"
    try:
        video_get = requests.get(url=m3u8_download_url, headers=headers)
        if video_get.status_code == 200:
            with open(f"file/video/{name}/{temp_filename}", "wb") as f:
                f.write(video_get.content)
            return (index, temp_filename)
        else:
            return (index, None)
    except Exception as e:
        return (index, None)


def merge_video_segments(temp_files, final_path):
    """合并所有视频片段到最终的文件"""
    with open(final_path, "wb") as final_file:
        for temp_file in temp_files:
            with open(temp_file, "rb") as f:
                final_file.write(f.read())
            os.remove(temp_file)  # 删除临时文件


def download_video_concurrently(findall, title, name):
    """并发下载视频片段，并按顺序合并"""
    video_dir = f"file/video/{name}"
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)

    final_path = f"{video_dir}/{title}.mp4"
    args = [(index, prefix_url + item, name, title) for index, item in enumerate(findall)]

    temp_files = [None] * len(findall)  # 存储临时文件名
    with ThreadPoolExecutor(max_workers=5) as executor:  # 最多同时下载5个片段
        futures = {executor.submit(download_segment, arg): arg[0] for arg in args}
        for future in tqdm(as_completed(futures), total=len(findall), desc="下载区段"):
            index, temp_file = future.result()
            if temp_file:
                temp_files[index] = f"{video_dir}/{temp_file}"

    # 确保所有片段都成功下载
    if all(temp_files):
        merge_video_segments(temp_files, final_path)
        print(f"{title} 视频成功合并到: {final_path}")
    else:
        print(f"{title} 某些片段下载失败，视频可能不完整.")


def main(url, name):
    # name 如果是空的就传时间
    if name == "":
        name = "A站"
    videoInfo, title = getVideoInfoAndTitle(url)
    findall = parseData(videoInfo)
    # downloadVideo(findall, title, name)
    download_video_concurrently(findall, title, name)


if __name__ == '__main__':
    main(url, name="")

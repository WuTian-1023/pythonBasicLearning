"""
    原始url: https://www.pearvideo.com/video_1167944
   梨视频禁用了视频播放页面的鼠标右键
    不知道具体的处理函数名，可以通过覆盖默认行为的方式：
    直接在浏览器控制台输入：
        document.addEventListener('contextmenu', function(event) { event.stopPropagation(); }, true);
    这会在捕获阶段添加一个监听器，阻止任何进一步的contextmenu事件处理。
    破解鼠标右击后获取正常播放的地址：https://video.pearvideo.com/mp4/short/20171027/cont-1167944-11048975-hd.mp4
                  接口返回的地址： https://video.pearvideo.com/mp4/short/20171027/1705894821911-11048975-hd.mp4
                  对比过后我们发现 1705894821911 -> cont-1167944  两者不同 1167944来自原始url
"""
# 1.拿到contId
# 2.拿到videoStatus 返回数据中的 srcUrl
# 3.拼接视频地址
# 4.下载视频
import requests

url = "https://www.pearvideo.com/video_1791379"
videoStatus = "https://www.pearvideo.com/videoStatus.jsp"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    # 防盗链 溯源 服务器会检查请求头中的referer是否是它自己的
    "Referer": url
}


# 拿到contId
def get_contId(url):
    # 1.拿到contId
    contId = url.split("_")[1]
    return contId


# 拿到videoStatus 返回数据中的 srcUrl
def get_srcUrl(contId):
    global videoStatus  # 全局变量
    # 2.拿到videoStatus 返回数据中的 srcUrl
    videoStatus = videoStatus + "?contId=" + contId
    videoStatus_get = requests.get(url=videoStatus, headers=headers)
    videoStatus_get.encoding = "utf-8"
    videoStatus_get_json = videoStatus_get.json()
    system_time = videoStatus_get_json["systemTime"]
    srcUrl = videoStatus_get_json["videoInfo"]["videos"]["srcUrl"]
    return srcUrl, system_time


# 拼接视频地址
def get_video_url(srcUrl, system_time, contId):
    # 3.替换url
    #  https://video.pearvideo.com/mp4/short/20171027/1705896514135-11048975-hd.mp4
    #  https://video.pearvideo.com/mp4/short/20171027/cont-1167944-11048975-hd.mp4
    download_url = srcUrl.replace(system_time, f"cont-{contId}")
    print(download_url)
    return download_url


# 下载视频
def download_video(video_url, contId):
    # 4.下载视频
    video_get = requests.get(url=video_url)
    video_get.encoding = "utf-8"
    video = video_get.content
    with open(f"file/video/梨视频{contId}.mp4", "wb") as f: # 保存视频 wb 二进制写入 防止视频损坏
        f.write(video)
    print("下载完成")


if __name__ == '__main__':
    contId = get_contId(url)
    ret = get_srcUrl(contId)
    src_url = ret[0]
    system_time = ret[1]
    video_url = get_video_url(src_url, system_time, contId)
    download_video(video_url, contId)

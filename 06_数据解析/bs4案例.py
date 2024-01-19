"""
 http://www.xinfadi.com.cn/index.html 原视频没有参考意义了
 目前数据是动态渲染的 接口地址: http://www.xinfadi.com.cn/getCat.html
 参数 prodCatid: 1186
"""
import requests

url = "http://www.xinfadi.com.cn/getCat.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

data = {
    "prodCatid": "1186"
}

requests_get = requests.get(url, headers=headers, params=data)
json = requests_get.json()
list = json["list"]
# 保存
f = open("file/text/新发地菜价.json", "w", encoding="utf-8")  # 保存json文件
for item in list:
    prodCat = item["prodCat"]
    prodName = item["prodName"]
    lowPrice = item["lowPrice"]
    highPrice = item["highPrice"]
    avgPrice = item["avgPrice"]
    unitInfo = item["unitInfo"]
    place = item["place"]
    specInfo = item["specInfo"]
    pubDate = item["pubDate"]
    # print(f"类型:{prodCat},名称:{prodName},最低价格:{lowPrice},最高价格:{highPrice},平均价格:{avgPrice},单位:{unitInfo},产地:{place},规格:{specInfo},发布时间:{pubDate}")
    f.write(
        f"类型:{prodCat},名称:{prodName},最低价格:{lowPrice},最高价格:{highPrice},平均价格:{avgPrice},单位:{unitInfo},产地:{place},规格:{specInfo},发布时间:{pubDate}\n")

# 关闭资源
f.close()
requests_get.close()
print("保存成功")

import time
from concurrent.futures import ThreadPoolExecutor
import requests
from tqdm import tqdm

"""
    确定url http://www.xinfadi.com.cn/getPriceData.html post 请求
    参数：
        limit: 20
        current: 2
        pubDateStartTime: 
        pubDateEndTime: 
        prodPcatid: 
        prodCatid: 
        prodName: 
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


# 获取网页数据
def get_data(current):
    data = {
        "limit": "20",
        "current": str(current)  # 确保传递的是字符串
    }
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    response = requests.post(url, headers=headers, data=data)
    response.encoding = "utf-8"
    print(response)
    return response.json()


# 解析数据
def parse_data(json_data):
    results = []
    for item in json_data["list"]:
        results.append((
            item["prodCat"], item["prodName"], item["lowPrice"],
            item["highPrice"], item["avgPrice"], item["unitInfo"],
            item["place"], item["specInfo"], item["pubDate"]
        ))
    return results


# 保存数据
def save_data(records):
    with open("file/text/新发地菜价.csv", "a", encoding="utf-8") as f:
        for record in records:
            f.write(
                f"类型:{record[0]},名称:{record[1]},最低价格:{record[2]},最高价格:{record[3]},平均价格:{record[4]},单位:{record[5]},产地:{record[6]},规格:{record[7]},发布时间:{record[8]}\n")
    print("保存成功")


# 主函数
if __name__ == '__main__':
    with ThreadPoolExecutor(3) as executor:
        futures = []
        for i in range(1, 4):  # 假设有3页数据需要抓取 温柔一点别被拉黑ip了
            future = executor.submit(get_data, i)
            futures.append(future)

        for future in tqdm(futures):
            json_data = future.result()  # 等待线程返回结果
            records = parse_data(json_data)
            save_data(records)
            time.sleep(1)  # 如果需要限制请求速度，可以保留这个延迟

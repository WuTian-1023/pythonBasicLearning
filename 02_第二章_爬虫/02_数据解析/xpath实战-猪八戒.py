"""
    1.确定url地址
    2.发请求获取页面数据
    3.解析数据
"""
import requests
from lxml import etree

url = "https://www.zbj.com/fw/?k=saas"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

requests_get = requests.get(url=url, headers=headers)
requests_get.encoding = "utf-8"
text = requests_get.text
# print(text)
# 3.解析数据
html = etree.HTML(text)
div_xpath = html.xpath("//div[@class='service-card-wrap']")
for item in div_xpath:
    # 获取店铺名 价格 商品名 评分 销量 好评
    shop_name = item.xpath("./div//div[@class='shop-detail']/div[@class='shop-info text-overflow-line']/text()") # 店铺名
    price = item.xpath("./div//div[@class='price']/span/text()")
    trade_name = item.xpath("./div//div[@class='name-pic-box'][1]/a/text()")
    Score = item.xpath("./div//div[@class='descprit-box']/div[@class='fraction']/span/span/text()")
    sale = item.xpath("./div//div[@class='sales']/span/div/span[2]/text()")
    comment = item.xpath("./div//div[@class='evaluate']/span/div/span[2]/text()")
    print(f"店铺名:{shop_name}, 价格:{price}, 商品名:{trade_name}, 评分:{Score}, 销量:{sale}, 好评:{comment}")
#     保存
    with open("file/text/猪八戒网.txt", "a", encoding="utf-8") as f:
        f.write(f"店铺名:{shop_name}, 价格:{price}, 商品名:{trade_name}, 评分:{Score}, 销量:{sale}, 好评:{comment}\n")

# 关闭文件
f.close()
requests_get.close()
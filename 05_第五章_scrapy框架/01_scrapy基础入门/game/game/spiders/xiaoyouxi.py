import scrapy


class XiaoyouxiSpider(scrapy.Spider):
    name = "xiaoyouxi"  # 爬虫名
    allowed_domains = ["4399.com"]  # 允许的域名
    start_urls = ["https://www.4399.com/flash/"]  # 起始url

    def parse(self, response):  # 解析函数
        # game_name = response.xpath("//ul[@class='n-game cf']/li/a/b/text()").extract() # 从网页中提取游戏名 extract
        #  <Selector query="//ul[@class='n-game cf']/li/a/b/text()" data='白方块过圆圈'> # 一个Selector对象
        # print(game_name)
        li_list = response.xpath("//ul[@class='n-game cf']/li")
        for item in li_list:
            name = item.xpath("./a/b/text()").extract_first()  # 提取游戏名
            category = item.xpath("./em/a/text()").extract_first()  # 提取游戏类别
            date = item.xpath("./em/text()").extract_first()  # 时间

            dic = {
                "name": name,
                "category": category,
                "date": date
            }
            yield dic  # 返回数据 yield: 生成器 作用：返回数据

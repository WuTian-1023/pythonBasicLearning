import scrapy
from caipiao.items import CaipiaoItem # 导入自己定义的实体类

class ShuangseqiuSpider(scrapy.Spider):
    name = "shuangseqiu"
    allowed_domains = ["500.com"]
    start_urls = ["https://datachart.500.com/ssq/"]

    def parse(self, response, **kwargs):
        # print(response.text)
        tr_list = response.xpath("//tbody[@id='tdata']/tr")
        for tr in tr_list:
            if tr.xpath("./@class").extract_first() == "tdbck":
                continue
            # chartBall01 chartBall02
            red_ball = tr.xpath("./td[@class='chartBall01']/text()").extract()  # 返回的是列表 红球
            blue_ball = tr.xpath("./td[@class='chartBall02']/text()").extract_first()  # 返回的是字符串 蓝球
            qh = tr.xpath("./td[1]/text()").extract_first()
            caipiao = CaipiaoItem(name="双色球", qihao=qh, red_ball=red_ball, blue_ball=blue_ball)
            yield caipiao

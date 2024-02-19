# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 类似Java的实体类
class CaipiaoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 彩票名称
    qihao = scrapy.Field()  # 期号
    red_ball = scrapy.Field()  # 红球
    blue_ball = scrapy.Field()  # 蓝球

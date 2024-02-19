# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TupianzhijiaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    img_src = scrapy.Field()
    # 添加新的字段以保存图片路径
    image_paths = scrapy.Field()

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

'''
    管道文件 默认关闭需要在settings.py中开启
    作用：对爬虫爬取的数据进行处理
    1. 数据清洗
    2. 数据存储
    3. 数据去重
    4. 数据验证
    5. 数据筛选
    6. 数据转换
'''


class GamePipeline:
    def process_item(self, item, spider):  # 处理item
        print(item)
        # print(spider.name)
        return item


class NewPipeline:
    def process_item(self, item, spider):  # 处理item
        # 网站名
        item['webname'] = "4399小游戏"
        return item

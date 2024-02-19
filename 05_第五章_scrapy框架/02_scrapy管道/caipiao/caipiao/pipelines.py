# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

'''
    数据存储的方案:
        1. 存储到数据库
        2. 存储到文件
        3. 存储到缓存
        4. 存储到搜索引擎
        5. 存储到其他服务器
'''


class CaipiaoPipeline:

    def open_spider(self, spider):
        print("爬虫开始了")
        self.f = open("双色球.csv", "a", encoding="utf-8")

    def close_spider(self, spider):
        print("爬虫结束了")
        if self.f:
            self.f.close()

    def process_item(self, item, spider):
        if self.f:
            self.f.write(f"{item['name']},{item['qihao']},{item['red_ball']},{item['blue_ball']}\n")
        return item


class MysqlPipeline:

    def open_spider(self, spider):
        import pymysql
        self.conn = pymysql.connect(
            host="localhost", user="root", password="123456", database="python", charset="utf8")
        self.cursor = self.conn.cursor()
        print("爬虫开始了")

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        print("爬虫结束了")

    def process_item(self, item, spider):
        # 将红球列表转换成逗号分隔的字符串
        red_ball_str = ','.join(item['red_ball'])
        # SQL语句
        sql = "insert into shuangseqiu(name, qihao, red_ball, blue_ball) values(%s, %s, %s, %s)"
        # 执行SQL语句，注意将红球列表转换后的字符串传递给SQL
        self.cursor.execute(sql, (item['name'], item['qihao'], red_ball_str, item['blue_ball']))
        self.conn.commit()
        return item


class MongDBPipeline:

    def open_spider(self, spider):
        from pymongo import MongoClient
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["caipiao"] # 创建数据库
        self.collection = self.db["shuangseqiu"] # 创建集合
        print("爬虫开始了")

    def close_spider(self, spider):
        self.client.close()
        print("爬虫结束了")

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

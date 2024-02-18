# --*-- conding:utf-8 --*--
# @Time : 2024-02-18 018 上午 11:25
# @Author : CoderTLL
# @Email : javacoder1023@gmail.com
# @File : 02_链家二手房.py
# @Software : PyCharm
# 代码不规范 同事两行泪
import datetime
import uuid

import requests

from lxml import etree
from pymongo import MongoClient
import pymysql


class LianjiaSpiderMongoDB:
    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host, port)  # 创建连接

    def get_html(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        return response.text

    def parse_html(self, html):
        ret = []
        data = etree.HTML(html)
        # 获取房源信息
        li_list = data.xpath('//ul[@class="sellListContent"]/li')
        '''
            我们需要的数据有：
                1. 标题
                2. houseInfo
                8. 位置
                9. 总价
                10. 单价
                11.多少人关注
                12. 发布时间
                13. 详情页链接
        '''
        for li in li_list:
            title = li.xpath('.//div[@class="title"]/a/text()')[0]  # 标题
            houseInfo = li.xpath('.//div[@class="houseInfo"]/text()')[0]  # 户型
            positionInfo_0 = li.xpath('.//div[@class="positionInfo"]/a/text()')[0]  # 位置
            positionInfo_1 = li.xpath('.//div[@class="positionInfo"]/a/text()')[1]  # 位置
            positionInfo = positionInfo_0 + '-' + positionInfo_1  # 位置
            # 去空格
            positionInfo = positionInfo.replace(' ', '')
            totalPrice = li.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')[0] + '万'  # 总价
            unitPrice = li.xpath('.//div[@class="unitPrice"]/span/text()')[0]  # 单价
            followInfo = li.xpath('.//div[@class="followInfo"]/text()')[0]  # 关注人数
            number_of_followers = followInfo.split('/')[0].strip()  # 关注人数
            release_time = followInfo.split('/')[1].strip()  # 发布时间
            detail_url = li.xpath('.//div[@class="title"]/a/@href')[0]  # 详情页链接
            dic = {
                'title': title,
                'houseInfo': houseInfo,
                'positionInfo': positionInfo,
                'totalPrice': totalPrice,
                'unitPrice': unitPrice,
                'number_of_followers': number_of_followers,
                'release_time': release_time,
                'detail_url': detail_url
            }
            ret.append(dic)
        return ret

    def save_mongo(self, list_data):
        try:
            mongoDB = self.client['lianjia']
            collection = mongoDB['changsha_ershoufang']
            collection.insert_many(list_data)
        except Exception as e:
            print(f"发生错误: {e}")

    def get(self, db_name, collection_name, condition):
        try:
            mongoDB = self.client[db_name]
            collection = mongoDB[collection_name]
            ret = collection.find(condition)
            for i in ret:
                print(i)
        except Exception as e:
            print(f"发生错误: {e}")

    def saveAll(self):
        i = 1  # 从第二页开始 第一页已经保存了
        url = f'https://cs.lianjia.com/ershoufang/pg{i}/'
        # 保存个100页的
        while i < 101:
            html = self.get_html(url)
            list_data = self.parse_html(html)
            self.save_mongo(list_data)
            print(f'第{i}页数据保存成功')
            i += 1
            url = f'https://cs.lianjia.com/ershoufang/pg{i}/'


class LianjiaSpiderMySQL:
    def __init__(self, host='localhost', port=3306, user='root', password='123456', database='python'):
        self.db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )

    def get_html(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        return response.text

    def parse_html(self, html):
        ret = []
        data = etree.HTML(html)
        # 获取房源信息
        li_list = data.xpath('//ul[@class="sellListContent"]/li')
        '''
            我们需要的数据有：
                1. 标题
                2. houseInfo
                8. 位置
                9. 总价
                10. 单价
                11.多少人关注
                12. 发布时间
                13. 详情页链接
        '''
        for li in li_list:
            title = li.xpath('.//div[@class="title"]/a/text()')[0]  # 标题
            houseInfo = li.xpath('.//div[@class="houseInfo"]/text()')[0]  # 户型
            positionInfo_0 = li.xpath('.//div[@class="positionInfo"]/a/text()')[0]  # 位置
            positionInfo_1 = li.xpath('.//div[@class="positionInfo"]/a/text()')[1]  # 位置
            positionInfo = positionInfo_0 + '-' + positionInfo_1  # 位置
            # 去空格
            positionInfo = positionInfo.replace(' ', '')
            totalPrice = li.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')[0] + '万'  # 总价
            unitPrice = li.xpath('.//div[@class="unitPrice"]/span/text()')[0]  # 单价
            followInfo = li.xpath('.//div[@class="followInfo"]/text()')[0]  # 关注人数
            number_of_followers = followInfo.split('/')[0].strip()  # 关注人数
            release_time = followInfo.split('/')[1].strip()  # 发布时间
            detail_url = li.xpath('.//div[@class="title"]/a/@href')[0]  # 详情页链接
            dic = {
                'id': str(uuid.uuid4()),
                'title': title,
                'houseInfo': houseInfo,
                'positionInfo': positionInfo,
                'totalPrice': totalPrice,
                'unitPrice': unitPrice,
                'number_of_followers': number_of_followers,
                'release_time': release_time,
                'detail_url': detail_url,
                'create_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            ret.append(dic)
        return ret

    def saveAll(self):
        i = 1  # 从第二页开始 第一页已经保存了
        url = f'https://cs.lianjia.com/ershoufang/pg{i}/'
        # 保存个100页的
        while i < 101:
            html = self.get_html(url)
            list_data = self.parse_html(html)
            self.insert(list_data)
            print(f'第{i}页数据保存成功')
            i += 1
            url = f'https://cs.lianjia.com/ershoufang/pg{i}/'

    def insert(self, list_data):
        # 插入数据
        cursor = self.db.cursor()
        sql = "INSERT INTO changsha_ershoufang (id, title, houseInfo, positionInfo, totalPrice, unitPrice, number_of_followers, release_time, detail_url, create_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for data in list_data:
            values = (
                data['id'], data['title'], data['houseInfo'], data['positionInfo'], data['totalPrice'],
                data['unitPrice'],
                data['number_of_followers'], data['release_time'], data['detail_url'], data['create_time'])
            cursor.execute(sql, values)
            # 提交
            self.db.commit()
        cursor.close()


if __name__ == '__main__':
    spider = LianjiaSpiderMongoDB()
    spider.saveAll()
    LianjiaSpiderMySQL().saveAll()

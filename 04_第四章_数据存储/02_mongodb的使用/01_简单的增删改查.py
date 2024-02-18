# --*-- conding:utf-8 --*--
# @Time : 2024-02-05 005 下午 05:54
# @Author : CoderTLL
# @Email : javacoder1023@gmail.com
# @File : 01_简单的增删改查.py
# @Software : PyCharm
# 代码不规范 同事两行泪
from pymongo import MongoClient


class MongoDB:
    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host, port)

    def create(self):
        # 创建数据库
        var = self.client['tll-coder']

    # 查询数据 
    '''
    db_name: 数据库名
    collection_name: 集合名
    condition: 查询条件
    '''

    def get(self, db_name, collection_name, condition):
        try:
            mongoDB = self.client[db_name]
            collection = mongoDB[collection_name]
            ret = collection.find(condition)
            for i in ret:
                print(i)
        except Exception as e:
            print(f"发生错误: {e}")

    # 插入数据
    '''
    db_name: 数据库名
    collection_name: 集合名
    data: 插入的数据
    '''

    def insert(self, db_name, collection_name, data):
        try:
            mongoDB = self.client[db_name]
            collection = mongoDB[collection_name]
            collection.insert_one(data)
        except Exception as e:
            print(f"发生错误: {e}")

    # 更新数据
    '''
    db_name: 数据库名
    collection_name: 集合名
    condition: 查询条件
    data: 更新的数据
    '''

    def update(self, db_name, collection_name, condition, data):
        try:
            mongoDB = self.client[db_name]
            collection = mongoDB[collection_name]
            collection.update_one(condition, {'$set': data},
                                  upsert=True)  # upsert=True 如果没有符合条件的数据，就插入一条新的数据 {'$set': data} 更新的数据
        except Exception as e:
            print(f"发生错误: {e}")

    # 删除数据
    '''
    db_name: 数据库名
    collection_name: 集合名
    condition: 查询条件
    '''

    def delete(self, db_name, collection_name, condition):
        try:
            mongoDB = self.client[db_name]
            collection = mongoDB[collection_name]
            collection.delete_one(condition)
        except Exception as e:
            print(f"发生错误: {e}")


if __name__ == '__main__':
    db = MongoDB()
    # 新增数据
    data = {'name': '安其拉', 'age': 34, 'password': '1231123'}
    db.insert('tll-coder', 'user', data)
    # 查询数据
    # condition = {'name': '李四'}
    condition = {'name': {'$regex': '^李'}}  # 查询名字以李开头的数据
    db.get('tll-coder', 'user', condition)
    # 修改数据
    condition = {'name': '李四'}
    data = {'name': '李四', 'age': 45, 'password': '1212122'}
    db.update('tll-coder', 'user', condition, data)
    # 删除数据
    condition = {'name': '李四'}
    db.delete('tll-coder', 'user', condition)

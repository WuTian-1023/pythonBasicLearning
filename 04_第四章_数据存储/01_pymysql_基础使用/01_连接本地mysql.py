# --*-- conding:utf-8 --*--
# @Time : 2024-02-02 002 下午 11:54
# @Author : CoderTLL
# @Email : javacoder1023@gmail.com
# @File : 01_连接本地mysql.py
# @Software : PyCharm
# 代码不规范 同事两行泪
import random

import pymysql


# 连接数据库
# host: 主机名
# user: 用户名
# password: 密码
# database: 数据库名
# port: 端口
# charset: 字符集
class Mysql:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            database='python',
        )

    def create_table(self):
        # 游标
        cursor = self.db.cursor()
        # 新建一张表 user
        sql = "create table user(id int, name varchar(20), age int, password varchar(20),  primary key(id))"
        cursor.execute(sql)
        cursor.close()

    def insert(self, id, name, age, password):
        # 插入数据
        cursor = self.db.cursor()
        # 获取id
        # 使用参数化查询和占位符
        sql = "INSERT INTO user (id, name, age, password) VALUES (%s, %s, %s, %s)"
        values = (id, name, age, password)
        cursor.execute(sql, values)  # 执行参数化查询
        # 提交
        self.db.commit()
        cursor.close()  # 关闭游标

    def select(self):
        # 查询数据
        cursor = self.db.cursor()
        sql = "select * from user"
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        cursor.close()

    def update(self):
        # 更新数据
        cursor = self.db.cursor()
        sql = "update user set name='张三' where id=3"
        cursor.execute(sql)
        self.db.commit()
        cursor.close()

    def delete(self):
        # 删除数据
        cursor = self.db.cursor()
        sql = "delete from user where id=3"
        cursor.execute(sql)
        self.db.commit()
        cursor.close()


if __name__ == '__main__':
    mysql = Mysql()
    try:
        # mysql.create_table()  # 创建表
        # print('创建成功')  # 创建成功
        rand_num = random.random()
        mysql.insert(id=rand_num, name="李四", age=18, password="88888888")  # 插入数据
        # mysql.update() # 更新数据
        # mysql.delete()  # 删除数据
        mysql.select()  # 查询数据
    except Exception as e:
        print(e)

# --*-- conding:utf-8 --*--
# @Time : 2024-02-03 003 上午 12:45
# @Author : CoderTLL
# @Email : javacoder1023@gmail.com
# @File : 02_SQLAlchemy_框架.py
# @Software : PyCharm
# 代码不规范 同事两行泪
# Alchemy [ˈælkəmi] n. 炼金术
# SQLAlchemy是Python编程语言下的一款开源软件。提供了SQL工具包及对象关系映射工具。
"""
SQLAlchemy是Python编程语言下的一款开源软件。提供了SQL工具包及对象关系映射工具。
https://docs.sqlalchemy.org/en/20/tutorial/engine.html # 官方文档
https://www.sqlalchemy.org/ # 官网
# 创建一个mysql引擎对象
# create_engine()的参数说明：
# dialect+driver://username:password@host:port/database
# dialect: 数据库类型
# driver: 数据库驱动
# username: 用户名
# password: 密码
# host: 主机名
# port: 端口
# database: 数据库名
# charset: 字符集
# echo: 是否打印日志
# pool_size: 连接池大小
# max_overflow: 连接池最大连接数
# pool_timeout: 连接池超时时间
# pool_recycle: 连接池回收时间
# pool_pre_ping: 是否开启连接检查
# pool_use_lifo: 是否使用LIFO队列
# connect_args: 连接参数

"""
import sqlalchemy as db
from sqlalchemy import create_engine

var = db.__version__  # 查看版本
print(var)  # 2.0.25
engine = db.create_engine("mysql+pymysql://root:123456@localhost:3306/python")
connect = engine.connect()
# 查看连接池
print(engine.pool.status()) # 连接池状态 Pool size: 5  Connections in pool: 1 Current Overflow: -4 Current Checked out connections: 0
data = db.MetaData()

t_user = db.Table('user', data, autoload_with=engine)

# 查询
select = db.select(t_user).order_by(db.desc(t_user.c.id)).limit(10)
result = connect.execute(select) # 执行查询
for row in result:
    print(row)

# 插入
insert = t_user.insert().values(id=4, name='张三', age=20 ,password='123456')
connect.execute(insert) # 执行插入
select_t_user__where = db.select(t_user).where(t_user.c.id == 4)
result = connect.execute(select_t_user__where) # 执行查询

# 更新
update = t_user.update().where(t_user.c.id == 4).values(name='李四')
connect.execute(update) # 执行更新
# 删除
delete = t_user.delete().where(t_user.c.id == 4)
connect.execute(delete) # 执行删除

# 关联查询
# 定义表
user = db.Table('user', data, autoload_with=engine)
address = db.Table('address', data, autoload_with=engine)

# 构造多表联查语句
join_statement = db.select(user.c.name, address.c.state, address.c.city, address.c.street).select_from(
    user.join(address, user.c.id == address.c.user_id))

# 执行查询
result = connect.execute(join_statement)

# 打印结果
for row in result:
    print(row)


# 关闭连接
connect.close()
engine.dispose() # 关闭连接池



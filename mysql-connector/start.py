#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""mysql-connector

可以直接创建数据库连接
或使用DBUtils建立连接池
"""

from dbutils.pooled_db import PooledDB
import mysql.connector

# 创建数据库连接池 - 基于mysql.connector
pool = PooledDB(mysql.connector, 5, host='127.0.0.1', user='root', password='123456', database='mysql')

# 从连接池中获取连接
conn = pool.connection()

# 直接创建数据库连接
# conn = mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password='123456',
#     database='mysql'
# )

# 获取游标对象
cur = conn.cursor()

# 执行sql语句
cur.execute('''SELECT * FROM user WHERE 1=1''')

# 获取查询结果
res = cur.fetchall()

# 遍历查询结果
for r in res:
    print(r)

# 关闭游标
cur.close()

# 关闭连接
conn.close()

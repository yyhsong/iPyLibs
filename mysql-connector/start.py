#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""mysql-connector

mysql-connector 是 MySQL 官方提供的驱动器
可以直接创建数据库连接，或使用DBUtils建立连接池

DBUtils is a suite of tools providing solid,
persistent and pooled connections to a database that can be used in all kinds of multi-threaded environments.
"""

from dbutils.pooled_db import PooledDB
import mysql.connector

# 创建数据库连接池 - 基于mysql.connector
pool = PooledDB(mysql.connector, 5, host='127.0.0.1', user='root', password='root', database='sys')

# 从连接池中获取连接
conn = pool.connection()

# 获取游标对象
cur = conn.cursor()

# 执行SQL语句
cur.execute('SELECT variable,value FROM sys_config WHERE 1=1')

# 获取查询结果
res = cur.fetchall()

# 遍历查询结果
for r in res:
    print(r)

# 关闭游标
cur.close()

# 关闭连接
conn.close()

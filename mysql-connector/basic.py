#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

# 创建数据库连接
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)

# 获取游标
cur = conn.cursor()

# 执行SQL语句
cur.execute('SHOW DATABASES')

for db in cur:
    print(db)

# 关闭游标
cur.close()

# 关闭连接
conn.close()

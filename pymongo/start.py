#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pymongo

NoSQL = Not only SQL
NoSQL常用于大规模数据的存储，具有高可扩展性、分布式计算、灵活架构、半结构化数据、没有复杂关系等特点
NoSQL包含列存储(HBase)、文档存储(MongoDB)、key-value对存储(Redis)、图存储(Neo4J)等分类

MongoDB是由C++语言编写的，一个基于分布式文件存储的开源数据库系统。
MongoDB旨在为WEB应用提供可扩展的高性能数据存储解决方案，使用的数据类型 BSON（类似 JSON）。
MongoDB将数据存储为一个文档，数据结构由键值(key=>value)对组成。MongoDB 文档类似于 JSON 对象。字段值可以包含其他文档，数组及文档数组。

RDBMS
- 使用二维表来组织数据，表具有预定义的结构和模式
- 使用结构化查询语言（SQL）进行数据查询和操作
- 支持ACID（原子性、一致性、隔离性和持久性）事务，保证数据的完整性和可靠性
- 适用于需要强一致性和复杂查询的应用

NoSQL
- 没有固定的结构，不使用表格，而是使用键值对、文档、列族或图形等方式存储数据
- 数据模型更灵活，可按需添加、删除和修改字段，适应快速变化的数据需求
- 通常使用各种编程语言的API进行数据操作，如JavaScript、Python等，而非SQL
- 提供水平扩展性，能够处理大规模的数据并支持高性能的读写操作
- 适用于需要处理大数据量、高并发、实时数据和快速可扩展性的场景，如社交媒体、物联网和日志处理
"""

import pymongo

# 建立数据库连接
mgclient = pymongo.MongoClient('mongodb://localhost:27017/')

# 获取已有库列表
dblist = mgclient.list_database_names()
print('Databases:', dblist)

# 使用指定数据库
curdb = mgclient['test']

# 获取集合列表
colist = curdb.list_collection_names()
print('Collections:', colist)

# 使用指定集合
curcol = curdb['users']

# 插入
doc = curcol.insert_one({'name': 'Neo', 'gender': 'male', 'age': 28})

# insert_data = [
#     {'name': 'foo', 'gender': 'male'},
#     {'name': 'bar', 'gender': 'male'}
# ]
# docs = curcol.insert_many(insert_data)
# print('Inserted:', len(docs.inserted_ids))

# 查询
res = curcol.find({}, {'_id': 0, 'name': 1, 'age': 1})  # 指定查询条件和查询字段
for r in res:
    print(r)

# 删除
x = curcol.delete_many({'gender': 'male'})  # 指定删除条件
print('Deleted:', x.deleted_count)

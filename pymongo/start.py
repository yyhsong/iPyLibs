#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pymongo

the Python driver for MongoDB
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
doc = curcol.insert_one({'name': 'Neo', 'gender': 'male', 'age': 33})

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

# NoSQL简介

NoSQL(NoSQL = Not Only SQL )，意即"不仅仅是SQL"，是对不同于传统的关系型数据库的数据库管理系统的统称。

NoSQL用于超大规模数据的存储。这种类型的数据存储不需要固定的模式，无需多余操作就可以横向扩展。

## 关系型数据库(RDBMS)遵循ACID原则

- A(Atomicity) 原子性
- C(Consistency) 一致性
- I(Isolation) 独立性
- D(Durability) 持久性

## 分布式系统

分布式系统（distributed system）由多台计算机和通信的软件组件通过计算机网络连接（本地网络或广域网）组成。

分布式系统是建立在网络之上的软件系统。正是因为软件的特性，所以分布式系统具有高度的内聚性和透明性。

因此，网络和分布式系统之间的区别更多的在于高层软件（特别是操作系统），而不是硬件。

分布式系统可以应用在不同的平台上如：PC、工作站、局域网和广域网上等。

- 分布式计算的优点：可靠性（容错性）、可扩展性、资源共享、灵活性、更快的速度、开放系统、更高的性能
- 分布式计算的缺点：故障排除、软件、网络、安全性

## RDBMS vs NoSQL

RDBMS
- 高度组织化结构化数据
- 结构化查询语言(SQL)
- 数据和关系都存储在单独的表中
- 数据操纵语言，数据定义语言
- 严格的一致性
- 基础事务

NoSQL
- 代表着不仅仅是SQL
- 没有声明性查询语言
- 没有预定义的模式
- 键/值对存储，列存储，文档存储，图形数据库
- 最终一致性，而非ACID属性
- 非结构化和不可预知的数据
- CAP定理：对于一个分布式计算系统来说，不可能同时很好地满足一致性、可用性及分区容错性
- 高性能，高可用性和可伸缩性

# MongoDB

MongoDB是一个基于分布式文件存储的数据库。

由C++语言编写，旨在为WEB应用提供可扩展的高性能数据存储解决方案。

MongoDB是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。

MongoDB采用文档存储的方式。文档存储一般用BSON（Binary JSON）格式存储，存储的内容是文档型的。
这样也就有机会对某些字段建立索引，实现关系数据库的某些功能。

## MongoDB中的基本概念

- 数据库 database
- 集合 collection, 类似table
- 文档 document, 类似row
- 域 field, 类似column
- 索引 index
- 主键 primary key, MongoDB自动将_id设置为主键，其值为ObjectId对象

## MongoDB基本指令

- 查看数据库 show dbs
- 创建/使用数据库 use db_name
- 查看集合 show collections
- 插入数据 db.collection_name.insert({...})
- 查询数据 db.collection_name.find().pretty()

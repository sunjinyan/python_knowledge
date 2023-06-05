#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', database='shop_user_srv')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from students")
# print(cursor.fetchone())
print(cursor.rowcount)

for i in  range(cursor.rowcount):
    print(cursor.fetchone())
# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])

# 获取最新自增ID
new_id = cursor.lastrowid
print(new_id)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
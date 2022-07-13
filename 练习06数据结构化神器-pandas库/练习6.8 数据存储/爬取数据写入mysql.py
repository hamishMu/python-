"""
select * from 数据表明 where 字段 like 内容
模糊查询 "%里巴%"

insert into 数据表名 （字段1，字段2）values(值1，值2)

删除
delete from  表名 where 字段 = 内容
"""

import pymysql
db = pymysql.connect(
    user='root',
    password='root',
    database='books',
    charset='utf8',
    host='localhost',
    port=3306
)

# 获取会话指针，并命为cur，调用sql语句，其中db为前面的数据库连接
cur = db.cursor()
# sql = 'insert into user(username,password) values("jack","passwd123")'
sql = 'select * from user '
cur.execute(sql)
data  = cur.fetchall()
print(data)
# 提交事务
db.commit()
cur.close()
db.close()




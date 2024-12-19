# 数据库

PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2 中则使用 mysqldb。  
PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。

## 准备环节

下载[MariaDB](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.6.2&os=windows&cpu=x86_64&pkg=msi&mirror=vhost_vn)  
安装PyMySQL   
```
pip install pymysql
```

## 导入库



```python
# Program
import pymysql
db = pymysql.connect(host='localhost',user='root',password='your-password',database='TESTDB')


```

## 游标对象
在数据库编程中，游标（Cursor）是一个非常重要的概念。游标对象用于帮助我们与数据库进行交互，特别是在执行查询操作时。


```python
# Program
curs_obj1 = db.cursor()

```

## 创建数据库表
如果数据库连接存在我们可以使用execute()方法来为数据库创建表，如下所示创建表EMPLOYEE：


```python
# Program
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
db = pymysql.connect(host='localhost',user='root',password='your-password',database='testdb')
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
 
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
 
cursor.execute(sql)
 
# 关闭数据库连接
db.close()
```

## CRUD操作
CRUD 是一个缩写，代表四种基本的数据库操作，它们是：  

- Create（创建）：指的是在数据库中插入新数据的操作。例如，向一个表中添加一条新的记录。  

- Read（读取）：指的是从数据库中检索数据的操作。这可以是查询单条记录，也可以是查询多条记录，甚至是整个表的数据。  

- Update（更新）：指的是修改数据库中已存在数据的操作。这通常涉及到更新表中的某些字段的值。  

- Delete（删除）：指的是从数据库中移除数据的操作。这可以是删除表中的一条记录，也可以是删除多条记录。  

CRUD 操作是数据库管理系统中最基本的操作，几乎所有的数据库应用都会涉及到这些操作。在编程和软件开发中，CRUD 操作通常被用来实现用户界面，允许用户对数据库中的数据进行增加、查询、修改和删除。  
### SQL插入语句


```python
# Program

# 重新连接数据库
db = pymysql.connect(host='localhost',user='root',password='your-password',database='TESTDB')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
#或者
'''
# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
       '''
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()
```

通过executemany()来插入多条数据


```python
# Program
sql_table = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)"
val_table=[('Mac', 'Mohan', 20, 'M', 2000)]

cursor.executemany(sql_table, val_table)
```

## 数据库更新操作
更新操作用于更新数据表的数据，以下实例将 TESTDB 表中 SEX 为 'M' 的 AGE 字段递增 1：


```python
# Program
#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
 
# 关闭数据库连接
db.close()
```

## 删除操作
删除操作用于删除数据表中的数据，以下实例演示了删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据：


```python
# Program
#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
 
# 关闭连接
db.close()
```

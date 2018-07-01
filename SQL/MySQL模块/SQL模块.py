"""
连接数据库登录, 与SQL注入
"""
import pymysql


name=input('username: ').strip()
pwd=input('password: ').strip()


# 登录
# # 连接数据库
# conn=pymysql.connect(host='127.0.0.1',user='root',password='123456',database='db1')
# #默认cursor(None) pymysql.cursors.DictCursor让结果1️以字典形式
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)#游标
# # sql="select * from userinfo where uname=%s and pwd=%s"
# # sql="select * from userinfo where uname=%(name)s and pwd=%(pwd)s"
# sql="select * from userinfo"
# # cursor.execute(sql,(name,pwd))#加载SQL
# cursor.execute(sql,{'name':name,'pwd':pwd})#加载SQL
# #fetchone()只能拿一条 fetchall()全部
# result=cursor.fetchall()#执行
# print(result)
# # 关闭数据库
# cursor.close()
# conn.close()
# if result:
#     print('登陆成功.')
# else:
#     print('登录失败.')

"""
增加
cursor.lastrowid 最后ID
"""
conn=pymysql.connect(host='127.0.0.1',user='root',password='123456',database='db1')
# conn=pymysql.connect(host='127.0.0.1',user='root',passwrod='123456',database='db1')
cursor=conn.cursor()
sql="insert into userinfo(uname,pwd) values(%(name)s,%(pwd)s)"
#r 受影响的行数
r=cursor.execute(sql,{'name':name,"pwd":pwd})
conn.commit()
print('最后ID:',cursor.lastrowid)
print('r',r)
cursor.close()
conn.close()

"""
新插入数据的自增ID
"""
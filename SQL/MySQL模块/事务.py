import pymysql
conn=pymysql.connect(host='localhost',user='root',password='123456',database='db1',charset='utf8')
curson=conn.cursor()
out=None;
#调用存储过程
curson.callproc('commit1',(out,))
conn.commit()
result = curson.fetchall()
print(result)

curson.execute('select @_commit1_0')

result = curson.fetchall()
print(result[0][0])
curson.close()
conn.close()



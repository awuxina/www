import pymysql
import time

# conn=pymysql.connect(host='localhost',user='root',password='123456',database='db1',charset='utf8')
# curson=conn.cursor()
# #调用存储过程
# curson.callproc('p1')
# conn.commit()
# result = curson.fetchall()
# print(result)
# curson.close()
# conn.close()


#带参数的存储过程
# conn=pymysql.connect(host='localhost',user='root',password='123456',database='db1',charset='utf8')
# curson=conn.cursor()
#
# #调用存储过程
# curson.callproc('p2',(1000,))
# conn.commit()
# result = curson.fetchall()
# print(result)
# curson.close()
# conn.close()



#带 参数和返回值 的存储过程
conn=pymysql.connect(host='localhost',user='root',password='123456',database='db1',charset='utf8')
curson=conn.cursor()
out=None;
#调用存储过程
curson.callproc('p3',(1000,out))
conn.commit()
result = curson.fetchall()
print(result)

curson.execute('select @_p3_0,@_p3_1')

result = curson.fetchall()
print(result)
curson.close()
conn.close()


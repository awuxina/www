""""""
"""
1.索引
    作用:
        - 约束
        - 加速查找
    索引:
        - 普通索引:加速查找
        - 主键索引:加速查找 + 不能为空 +不能重复
        - 唯一索引: 加速查找 +不能重复
        - 联合索引(多列): 
                - 联合主键索引
                - 联合唯一索引
                - 联合普通索引
    加速查找:
        快: select * from userinfo where name='asdf'
        假设
            id name email
            ....
            无索引:从前到后依次查找   
            索引:
                id          创建额外文件(特定格式存储)         
                name        创建额外文件(特定格式存储)         
                email       创建额外文件(特定格式存储)         
            创建索引:create index ix_name on userinfo(email);
                     普通索引 create index index unique 索引名称 on 表(列);
                     唯一索引 create unique index unique 索引名称 on 表(列);
                     组合索引:create unique index 索引名称 on 表(列1,列2)
                              - (name,email)
                                    select * from userinfo where name='aa' and email='fff';
                                    select * from userinfo where name='aa';
                              - 最左前缀匹配
                     索引合并:
                              - name
                              - email
                                     select * from userinfo where name='aa' and email='fff';
                                     select * from userinfo where name='aa';
                                     select * from userinfo where email='fff';        
                效率 组合索引 > 索引合并                                    
            索引种类:
                hash索引:     索引表
                btree索引:    二叉树
            建立索引:
                - 1.额外的文件保存特殊的数据结构
                - 2.查询快,但插入更新慢
                - 3.命中索引
                        select * from userinfo where email = 'asd';
                        select * from userinfo where email like 'asd';慢
            名词:                        
                覆盖索引:
                    - 在索引文件中直接获取数据的SQL                                                
                索引合并:                
                    - 把多个单列索引合并的使用
"""
import pymysql
import random
import time
start=time.time()
#随机输入 账户和密码
i=1
str=[chr(i) for i in range(ord('a'),ord('z')+1)]
while i<=100:
    name=''.join(random.sample(str,random.randint(1,18)))
    pwd=''.join(random.sample(str,random.randint(1,18)))
    conn=pymysql.connect(host='127.0.0.1',user='root',password='123456',database='db1',charset='utf8')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql="insert into userinfo(uname,pwd) values(%(name)s,%(pwd)s)"
    r=cursor.execute(sql,{'name':name,'pwd':pwd})
    conn.commit()
    if r:
        print('第{i}条'.format(i=i))
        i+=1
cursor.close()
conn.close()
print('用时:',time.time()-start)
#随机输入 账户和密码 END





# start=time.time()
# conn=pymysql.connect(host='127.0.0.1',user='root',password='123456',database='db1',,charset='utf8')
# cursor=conn.cursor()
# sql="select * from userinfo limit 100"
# r=cursor.execute(sql)
# cursor.fetchall()
# print('用时:',time.time()-start)
#
# start=time.time()
# sql="select * from userinfo WHERE id>0 limit 100"
# r=cursor.execute(sql)
# cursor.fetchall()
# print('用时:',time.time()-start)
# cursor.close()
# conn.close()
# 查询验证速度
#

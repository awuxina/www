import socket
import time
def f1(request):
    """
    处理用户请求,返回相应内容
    :param request: 用户请求的所有信息
    :return:
    """
    f = open(r'静态网站/index.html','rb')
    data=f.read()
    f.close()
    return bytes(data, encoding='utf8')
def f2(request):
    f = open(r'静态网站/aricle.html', 'r',encoding='utf8')
    data = f.read()
    f.close()
    ctime=time.time()
    data = data.replace('@@sw@@',str(ctime))
    return bytes(data,encoding='utf8')

def f3(request):
    import pymysql
    f = open(r'动态网站/host.html', 'r', encoding='utf8')
    data = f.read()
    f.close()

    conn = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='db1')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select id,uname,pwd,age from userinfo WHERE id>0 limit 10"
    cursor.execute(sql)
    user_list=cursor.fetchall()
    cursor.close()
    conn.close()
    from jinja2 import Template
    template= Template(data)
    data= template.render(xxxxx=user_list,user='aaa')
    return bytes(data, encoding='utf8')

routers =[
    ('/xxx',f1),
    ('/ooo',f2),
    ('/host',f3)
]

def run():
    sock =socket.socket()
    sock.bind(('127.0.0.1',8080))
    sock.listen(5)
    while True:
        conn,addr=sock.accept()
        data=conn.recv(8096)
        start = time.time()
        data = str(data,encoding='utf8')
        headers,bodys=data.split('\r\n\r\n')
        temp_list = headers.split('\r\n')
        method,url,protocal=temp_list[0].split(' ')
        conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
        func_name = None
        for item in routers:#item 就是routers 每一项
            if item[0] == url:
                func_name=item[1]
                # print('item[0]=',item[0])
                # print('item[1]=',item[1])
                break;
        if func_name:
            response=func_name('1')
        else:
            response=b'404'

        conn.send(response)
        conn.close()

        print('用时:', time.time() - start)

if __name__ == '__main__':
    run()
import socket
#socket.AF_INET 网络通讯套接字,SOCK_STREAM代表TCP协议,SOCK_DGRAM代表UDP协议
#生产一个客服端,相当一个手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#端口被占用时重启
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#设置端口重用

#定位,相当绑定手机卡
phone.bind(('127.0.0.1',8080))

#启动,手机开机,同时接收5个客户端
phone.listen(5)


#等待电话链接
print('等待中......')
while True:#链接循环
    conn,addr=phone.accept()
    print('电话线路',conn)
    print('客户端的手机号',addr)

    while True:#通讯循环
        try:
            #接收消息,一次最大接收1024个字节
            data=conn.recv(1024)
            if not data:break    #客户端单方面断开连接linx系统会无限收空,所以需要断开
            print('客服端消息:',data)
            #回复消息
            conn.send(data.upper())
        except Exception:
            break
    #挂断电话
    conn.close()
#关闭手机
phone.close()
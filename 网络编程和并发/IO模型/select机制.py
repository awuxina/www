#I/O多路复用
import socket
import select
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen(5)
sock.setblocking(False)  # 非阻塞套接字
inputs = [sock, ]
while True:
    r, w, e = select.select(inputs, [], [])  # 监听有变化的对象,r存放有变化的对象
    for obj in r:
        if obj == sock: #如果变化的是sock,即1个请求连接
                conn, addr = obj.accept()
                inputs.append(conn)
        else:   #如果变化的是conn,即一条消息
            try:
                data = obj.recv(1024)
                if not data:
                    id = inputs.index(obj)
                    inputs[id].close()
                    inputs.pop(id)
                print(data.decode('utf-8'))
                obj.send(data.upper())
            except Exception as e:
                #所有conn公用1个sock,当客户端断开连接时候,只需要关闭服务conn并删除
                id=inputs.index(obj)
                inputs[id].close()
                inputs.pop(id)



inputs[0].close()






#基于select模块实现的IO多路复用,建议使用
import selectors
import socket
socket=socket.socket()
socket.bind(('127.0.0.1', 8080))
socket.listen(5)
socket.setblocking(False)#设为非阻塞

#根据具体平台选择最佳IO多路机制,比如在linux,选择epoll
sel=selectors.DefaultSelector()

def read(conn,mask):
    try:
        data=conn.recv(1024)
        if not data:
            conn.close()
            sel.unregister(conn)
        print(data.decode('utf8'))
        conn.send(data.upper())
    except Exception:
        conn.close()
        sel.unregister(conn)#取消监听

def accpet(socket,mask):
    conn,addr=socket.accept()
    sel.register(conn, selectors.EVENT_READ, read)#注册监听
#第一个参数监听对象,第二个参数记住就好,第三个参数处理函数
sel.register(socket,selectors.EVENT_READ,accpet)    #注册监听

while True:
    events = sel.select()   #开始监听,返回有变化的对象[(key1,mask),(key2,mask)....]
    for key,mask in events:
        func=key.data   #key.data对应 accept 或 read
        obj=key.fileobj#key.fileobj对应socket
        func(obj,mask)  #调用 accpet(socket,mask) 或 read(coon,mask):
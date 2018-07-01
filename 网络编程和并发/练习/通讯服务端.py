import socket
import selectors
import json
# 加载1个 打包工具
import struct

sock=socket.socket()
sock.bind(('127.0.0.1',8080))
sock.listen(5)
sock.setblocking(False) #忘记

#选择监听实现方式
sel=selectors.DefaultSelector() #忘记

def close_io(conn):
    conn.close()
    sel.unregister(conn)

def read(conn,mark):
    try:
        #接收报头
        pack=struct.unpack('i',conn.recv(4))
        json_len=pack[0]
        print(pack[0])
        if not json_len:
            close_io(conn)
        else:
            #接收json
            json_content= json.loads(conn.recv(json_len).decode('utf8'))
            #解读内容
            print(conn.recv(json_content['size']).decode('utf8'))
    except Exception:
        close_io(conn)

def accept(sock,mark):
    conn,addr=sock.accept()
    sel.register(conn, selectors.EVENT_READ, read) #忘记

#监听器 使用
sel.register(sock, selectors.EVENT_READ, accept) #忘记

while True:
    events=sel.select()
    for key,mark in events:
        func=key.data
        obj=key.fileobj #忘记
        func(obj,mark)


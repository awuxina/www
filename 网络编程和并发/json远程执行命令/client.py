import socket
import struct
import json
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>:').strip()
    if not cmd:continue #如果输入是空这进入下次循环
    # phone.send(bytes(cmd.encode('utf-8')))
    phone.send(bytes(cmd,encoding='utf-8'))
    data=phone.recv(1024)
    print(data)
phone.close()
# import socket
# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# phone.connect('127.0.0.1',8080)
# phone.send('hello'.encode('utf-8'))
# phone.send('SB')
# data=phone.recv(1024)
# print(data.decode('gbk'))
# phone.close()

import struct
a=struct.pack('i',13212)
print(a)
import socket
udpserver=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpserver.bind(('127.0.0.1',8080))
while True:#通讯循环
    data,client_addr=udpserver.recvfrom(1024)
    print('客户端',data.decode('utf-8'))
    msg=input('>>:')
    udpserver.sendto(msg.encode('utf-8'),client_addr)

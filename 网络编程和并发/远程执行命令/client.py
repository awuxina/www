import socket
import struct
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>:').strip()
    if not cmd:continue #如果输入是空这进入下次循环
    # phone.send(bytes(cmd.encode('utf-8')))
    phone.send(bytes(cmd,encoding='utf-8'))

    #收报头
    baotou=phone.recv(4)
    data_size=int(struct.unpack('i',baotou)[0])
    print(data_size)
    #收数据
    recv_size=0
    recv_data=b''
    while recv_size<data_size:
        data=phone.recv(1024)
        recv_size+=len(data)
        recv_data+=data
    print(recv_data.decode('gbk'))#因为服务端是放在win win默认gbk linux 'utf-8'
phone.close()
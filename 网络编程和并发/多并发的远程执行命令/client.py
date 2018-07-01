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

    #part1:收报头长度
    head_struct = phone.recv(4)
    head_len = struct.unpack('i',head_struct)[0]
    #part2:报头长度
    head_bytes=phone.recv(head_len)
    head_json=head_bytes.decode('utf-8')
    head_dic=json.loads(head_json)

    #part3:收数据
    #收报头
    data_size = head_dic['data_size']

    #收数据
    recv_size=0
    recv_data=b''
    while recv_size<data_size:
        data=phone.recv(1024)
        recv_size+=len(data)
        recv_data+=data
    print(recv_data.decode('gbk'))#因为服务端是放在win win默认gbk linux 'utf-8'
phone.close()
import socket
import struct
import json
sock=socket.socket()
sock.connect(('127.0.0.1',8080))
while True:
    msg=input('>>:').strip()
    if not msg: continue  # 如果输入是空这进入下次循环
    str_len=len(msg)
    data = {'size': str_len}
    json_str=json.dumps(data)
    # 发送报头
    json_len = struct.pack('i', len(json_str))
    sock.send(json_len)
    #发送json
    sock.send(json_str.encode('utf8'))
    #发送内容
    sock.send(msg.encode('utf8'))
sock.close()

import socket
udpclient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_ip_port=('127.0.0.1',8080)
while True:
    inp=input('>>:')
    udpclient.sendto(inp.encode('utf-8'),server_ip_port)
    data,server_addr=udpclient.recvfrom(1024)
    print(data.decode('utf-8'))
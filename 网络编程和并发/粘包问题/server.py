import socket
import time
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8080))
phone.listen(5)
conn,addr=phone.accept()

data1=conn.recv(1)
time.sleep(5)
data2=conn.recv(1024)

# phone.close()
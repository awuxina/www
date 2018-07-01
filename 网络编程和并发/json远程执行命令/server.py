#服务端特点:
    #链接循环(提供服务)
    #通讯循环
import socket
import subprocess
import struct
import json
#socket.AF_INET 网络通讯套接字,SOCK_STREAM代表TCP协议,SOCK_DGRAM代表UDP协议
#生产一个客服端,相当一个手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#端口被占用时重启
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#设置端口重用

#定位,相当绑定手机卡
phone.bind(('127.0.0.1',8080))

#启动,手机开机,同时接收5个客户端
phone.listen(5)


#等待电话链接
print('json等待中......')
while True:#链接循环
    conn,addr=phone.accept()
    while True:#通讯循环
        try:
            #接收消息,一次最大接收1024个字节
            cmd=conn.recv(1024)
            if not cmd:break    #客户端单方面断开连接linx系统会无限收空,所以需要断开
            #执行命令
            res=subprocess.Popen(cmd.decode('utf-8'),
                                 shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
            out_res=res.stdout.read()
            err_res=res.stdout.read()
            data_size=len(out_res)+len(err_res)
            head_dic = {'data_size': data_size}
            head_json = json.dumps(head_dic)
            head_bytes = head_json.encode('utf-8')
            #part1:发报头的长度
            head_len=int(len(head_bytes))
            conn.send(struct.pack('i',head_len))
            #part2:发送报头
            conn.send(head_bytes)
            #part3:发送内容
            conn.send(out_res)
            conn.send(err_res)#如果有错误消息会回复给客户端,没有发空,操作系统见空自动不发
        except Exception as e:
            # print(e)
            raise e
            break
    #挂断电话
    conn.close()
#关闭手机
phone.close()
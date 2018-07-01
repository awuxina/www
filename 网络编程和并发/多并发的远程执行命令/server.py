import socketserver
#多客服端通讯必须继承socketserver.BaseRequestHandler类
# 1.sock.socket               用于传入请求的套接字对象
# 2.sock.server_address       监听服务器的地址.比如元组("127.0.0.1",80)
# 3.sock.RequestHandlerClass  传递给服务器构造函数并由用户提供的请求处理程序类.
# 4.sock.serve_forever()      处理无限的请求.
# 5.sock.shutdown()           停止serve_forever()循环.
# 6.sock.fileno()             返回服务器套接字的整数文件描述符.该方法可以有效的通过轮询操作(如select()函数)使用服务器实例.
class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print("from conn:",self.request)
        while True:
            data=self.request.recv(1024)
            if not data: break
            print(data)
            self.request.send(data.upper())


s1=socketserver.ThreadingTCPServer(("127.0.0.1",8080),MyServer)
s1.serve_forever()
























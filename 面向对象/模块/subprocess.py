# import subprocess
# mode = 'host'
#
# # 本地执行cmd命令
# if mode =='host':
#     v1 = subprocess.getoutput('ipconfig')
#     print(v1)
#
# # # 远程执行cmd命令
# elif mode=='ssh':
#     # paramiko 是一台中控机 主动发送命令获取结果
#     import paramiko
#     # private_key= paramiko.RSAKey.from_private_key_file('xxx')
#     # 创建ssh 对象
#     ssh = paramiko.SSHClient()
#     # 允许连接不在know_hosts 文件中的主机
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     # 连接服务器
#     # ssh.connect(hostname='minion1',port=22,username='root',pkey=private_key)
#     ssh.connect(hostname='192.168.0.101',port=22,username='root',password='lantao')
#     # 执行命令
#     # stdin 当操作需要进一步命令式时 写入
#     # stdout 结果
#     # stderr 命令出错时信息
#     stdin,stdout,stderr = ssh.exec_command('rm')
#     result = stdout.read().decode('utf8')
#     ssh.close()
#     print('结果:',result)
#     print('下一步提示:',stdin)
#     print('错误',stderr.read().decode('utf8'))
#
#
# else:
#     v1 = subprocess.getoutput('ifconfig')
#

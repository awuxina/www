# 流程:
#       1:  打开文件: open()
#       2:  操作文件:
#       3:  关闭文件:close()

# read(1)    代表读第1个字节
# tell()     当前指针的位置
# writable() 是否可写
# readable() 是否可读
# flush()    将内容立刻放到硬盘
# readline() 读取一行
# truncate() 根据当前指针位置截取前面部分,后面丢弃
# .seek(0)   光标移动到0位置,seek 按字节移动
# .seek(-3,2) 光标移动到-3个位置,第二参数默认0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起,但1,2只能在rb、wb、ab模式下操作
# 读取utf-8格式数据,转换成unicode(str)编码的数据

#文件重命名
#import os
#os.rename()
#文件重命名  END

# \r将光标移动到开始位置
# \n换行
# \r\n光标移动到下一行


# obj = open('用于读取的文件.txt',encoding='utf-8',mode='r')
# centent = obj.read()
# obj.close()
# print(centent,type(centent))

# 读取数据,转换成bytes编码的数据,此方式用于上传和下载文件
# obj = open('用于读取的文件.txt',mode='rb')
# centent = obj.read()
# obj.close()
# print(centent,type(centent))

# 用utf-8格式写文件
# obj = open('用于写入的文件.txt',mode='w',encoding='utf-8')
# obj.write('第一行\n')
# obj.close()

# #用utf-8格式追加写文件
# obj = open('用于写入的文件.txt',mode='a',encoding='utf-8')
# obj.write('第一行\n')
# obj.close()

# 用utf-8格式能读,能追加写模式,写入自定位置
# obj = open('用于写入的文件.txt',mode='r+',encoding='utf-8')
# content = obj.read(1)
# #指定位置写入
# obj.seek(obj.tell())
# obj.write('7')
# obj.close()
# print(content)

# #用utf-8格式可读可写,追加模式  r+   w+  a+
# r+追加写人,默认光标开始位置
# w+重写,光标默认在最后
# a+光标默认在最后,如果要读取需要移动光标
# obj = open('text2.txt',mode='r+',encoding='utf-8')
# print(obj.read(1))
# obj.seek(0)
# print(obj.read())
# # obj.write('666斯蒂芬噶分阿达我我')
# obj.close()


# ---------------rb wb ab 文件基于bytes操作  r w b模式就是操作系统自动做了这里的操作
# obj = open('text2.txt',mode='rb')
# print(obj.read())
# obj.close()

# obj = open('text2.txt',mode='wb')
# obj.write('hello李杰'.encode('utf8'))
# obj.close()

# ---------------rb wb ab 文件基于bytes操作

# 直接使用open close 在close之前的系统操作文件都没有立刻输入到磁盘,需要手动.flush(),为了避免麻烦采取第二种方式
# with控制块 文件处理
# with结束就自动关闭保存文件
# with open('text2.txt') as f: # 等价于:f=open('text2.txt')
#     f.read()
# with控制块 文件处理  END

# 操作haproxy.conf文件 查找
# l=[]
# falg=False
# while True:
#     m=input('请输入链接:').strip()
#     if m=='no':
#         break
#     with open('haproxy.conf', encoding='utf8') as f:
#         for line in f:
#             if line.startswith('backend'):
#                 if m in line:
#                     falg = True
#                     continue
#                 break
#             if falg:
#                 l.append(line.strip())
#         for i in l:
#             print(i)
# 操作haproxy.conf文件 查找 END


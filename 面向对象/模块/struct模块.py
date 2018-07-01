import struct
s=struct.pack('i',123123)#将数字转成固定长度
s1=struct.unpack('i',s)[0]#解码
print(s,s1)
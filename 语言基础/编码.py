# -*- coding:utf-8 -*-

name ='中国'
print(name)
print(name.encode('GBK')) #目标编码
print(len(name.encode('utf8')))



#在py3中数据存在硬盘上或网络发送都是bytes格式
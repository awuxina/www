# #长度
# print(len("aaa"))

# #查看数据类型
# print(type(1))

#左边如果为true,a=值.如果左边为假,左边为真结果为true,右边为假则false
#a = 1>3 or 2>1
#print(a)

# #2转换为6个直接字节
# val=2
# result = val.to_bytes(6,'big')
# print(result)

#判断是否为数字
#print('123'.isdecimal())

#二进制长度
# a=11
# print(a.bit_length())

#字符转数字
# a='11'
# print(int(a))
###################字符串函数#######################
# #字符串分割
# print("advbds".split('v',1))

#字符串大写
#print('alex'.upper())

#字符串小写
#print('ALex'.lower())

# #首字母大写
# print("首字母大写"+"alex".capitalize())

#去除两边空白
#print('  adfa   '.strip())

#去除左边空格
#print('  adfa   '.lstrip())

#去除右边空格
#print('  adfa   '.rstrip())

#替换
#print('我要在这里使用替换了,要在这里使用')
#替换,第三参数代表要替换几次
#print('我要在这里使用替换了,要在这里使用'.replace('要在','马上',1))

#分割
#print('我要在这里使用替换了,要在这里使用'.split('在'))
#分割,第二个参数代表分割几次
#print('我要在这里使用替换了,要在这里使用'.split('在',1))

# #宽度左右填充
# print('alEx'.center(20,'*'))
# #宽度左填充
# print('alEx'.ljust(20,'*'))
# #宽度右填充
# print('alEx'.rjust(20,'*'))

# #查找元素出现次数
# print('fadvbsrfadae'.count('ad'))
# #查找元素出现次数,可设置开始和结束位置
# print('fadvbsrfadae'.count('ad',0,5))
#查找
# print('sdfsadfea'.find('f'))

#字符串转换成指定编码
# print('啊啊'.encode('utf8'))

#指定tab的宽度
# print('我是啊爱的啊\t速\n度烦我啊死我\t阿萨德分'.expandtabs(7))

#字符串格式化
# print('我叫{0},年龄{1}'.format("哈哈",31))
# print('我叫{0},年龄{1}'.format(*["哈哈",31]))
# print('我叫{name},年龄{age}'.format(name='哈哈',age=31))
# print('我叫{name},年龄{age}'.format(**{'name':'哈哈','age':31}))
# print('我叫{name},年龄{age}'.format_map({'name':'哈哈','age':31}))

# name = "zhangsan,lisi,wangwu"
# #切片
# print(name[0:8])
# #反切
# print(name[-6:-1])
# #反切到尾部
# print(name[-6:])
# #步长切片
# print(name[0::3])
###################字符串函数 END#######################




###################列表函数#######################
v = [11,22,33,44,1,'是我',11,88]
#尾部追加
#v.append('哈哈')
#批量追加
# v.extend([55,66,77])
# v.extend('礼券')

#指定位置插入数据
#v.insert(1,'啊啊')

#删除索引位置
#del v[0]
#删除指点长度
#del v[1:3]
#删除并返回一个删除值
#new =v.pop()
#删除指定索引的值并返回一个删除值
# new =v.pop(0)
#删除指定值,如果有重复删除第一个
# new =v.remove(11)
# print(new)

#批量赋值,字符串每个字符会一一赋值
#v[2:4]="吴国成"
#批量赋值 字符串会作为1个值赋值
#v[2:4]=["吴国成",]

#数组倒转
#v.reverse()

#清空
#v.clear()

#复制,不同时指向同一个地址
# new = v.copy()
# new.append(55)
# print(new)
#复制,同时指向同一个地址
# new = v
# new.append(55)
# v.append(66)
# 深复制 新版好像无意义
# import copy
# v.append([99,100])
# new = copy.deepcopy(v)
# print(new)

#排序从小到大,默认recerse=False
# v.sort()
#排序从大到小
# v.sort(reverse=True)

#查找，反悔索引
#v=v.index(1)

#统计出现次数
#v=v.count(11)
#print(v)
###################列表函数 END#######################

#######################字典 END#######################
v={'k1':'v1','k2':'v2'}
#根据键找值
#不建议使用,不存在则报错
# print(v['k1'])
#建议使用
# print(v.get('k1'))

#找到所有键
# print(v.keys())

#找到所有值
# print(v.values())

#找到所有数据
# print(v.items())

#添加数据
#v['s1']='ss'
#print(v)

#循环读取所有数据 不要用效率低
# for k,v in v.items():
#     print(k+':'+v)

#删除
#print(v.pop('k1'))
#或
# del v['k1']
# print(v)
#删除不存在字段报错,可添加1个值返回该值
#print(v.pop('k11',"none"))

#判断是否存在字典中
#print(113 in v)

#更新字典
# dict2={1:'aaa',2:"bbb",'k1':'KKKKK'}
# v.update(dict2)
# print(v)
#######################字典 END#######################

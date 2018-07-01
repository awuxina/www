# -*- coding:utf-8 -*-
name = 'My name is {0},\t i am {1} yese old'
name2 = 'my name is {name},my i am {age} years old'
#常用strip center count find lower upper  join split endswith replace index
#字符串大小写
#print(name.upper())                        #把所有字符中的小写字母转换成大写字母
#print(name.lower())                        #把所有字符中的大写字母转换成小写字母
#print(name.capitalize())                   #把第一个字母转化为大写字母，其余小写
#print(name.title())                        #把每个单词的第一个字母转化为大写，其余小写
# print(name.swapcase())                    #大小写互换
#字符串大小写 END
#print(name.center(20,'-'))                 #长度20,不够用'-' 填充
#print(name2.ljust(50,'-'))                 #左对齐不够用'-' 填充
# print(name2.rjust(50,'-'))                #左对齐不够用'-' 填充
# print(name2.strip('my'))                  #移除1个'my'
#print(name2.lstrip('my'))                  #只左边移除'my'
#print(name2.rstrip('my'))                  #只右边移除'my'
#print(name.count('e'),3,7)                 #统计3出现次数,第3个位置开始第7位置结束
#print(name.endswith('LI'))                 #是否'LI'结尾
#print(name.expandtabs(15))                #\t的长度
#print(name.format('alex',22))              #填充数据
#print(name2.format(name='alex',age=22))    #填充数据
#print(name2.format_map({'name':'alex','age':22}))  #填充数据
#print(name.find('e'),3)                    #从第3个位置,查找'e'所在的索引,找不到返回-1
# print(name2.rfind('s'))                   #从右边开始找
#print(name.index('is'))                    #查找'is'的位置,找不到会报错
#print(name.startswith('name',3,10))        #从第3个位置开始到第10个位置结束,查找'name'并且以name开头
#print('ada'.isalnum())                     #'ada'是不是字符或者数字
#print('101'.isdecimal())                   #'101'是不是1个正整数
#print('-1'.isnumeric())                    #'-1'是不是1个正整数
#print('a1'.isalpha())                      #'a1'是不是全是字母
#print('a'.isidentifier())                  #'a'是不是1个合法的关键字,即:是不是合法变量名
# print('a'.isprintable())                  #字符串能不能打印
# print(' '.isspace())                      #是不是空格
# print('Today Headline'.istitle())         #是不是标题 即:所有单词首字母大写
# print('||||'.join(['a','cd','ef']))       #把列表拼接成字符串用'||||'隔开
# print(name2.replace('my','me'))           #把'my'全替换成'me'
# print(name2.replace('my','me',1))           #把'my'全替换成'me',只换1次

#将字符串'abcde'一一对应替换成'12345'
# IN = 'abcde'
# OUT = '12345'
# trans_table = str.maketrans(IN, OUT)
# print(name2.translate(trans_table))
#将字符串'abcde'一一对应替换成'12345' END
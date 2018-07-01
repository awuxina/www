import re
#   .   匹配任何1个除换行符以外的任何符号
#   \   转义字符，使后一个字符改变原来的意思
#   +   匹配前一个字符1次或无限次
#   ?   匹配一个字符0次或1次
#   ^   匹配字符串开头。在多行模式中匹配每一行的开头
#   $   匹配字符串末尾，在多行模式中匹配每一行的末尾
#  |	或。匹配|左右表达式任意一个，从左到右匹配，如果|没有包括在()中，则它的范围是整个正则表达式
#   {m,n}	{m}匹配前一个字符m次，{m,n}匹配前一个字符m至n次，若省略n，则匹配m至无限次
#   []  字符集。对应的位置可以是字符集中任意字符。
#               字符集中的字符可以逐个列出，也可以给出范围，如[abc]或[a-c]。[^abc]表示取反，即非abc。
#               所有特殊字符在字符集中都失去其原有的特殊含义。用\反斜杠转义恢复特殊字符的特殊含义。
#   ()  被括起来的表达式将作为分组，从表达式左边开始没遇到一个分组的左括号“（”，编号+1.
#           分组表达式作为一个整体，可以后接数量词。表达式中的|仅在该组中有效。

#   \d  数字:[0-9]
#   \D  非数字:[^\d]
#   \s  匹配任何空白字符:[<空格>\t\r\n\f\v]
#   \S  非空白字符:[^\s]
#   \w  匹配包括下划线在内的任何字字符:[A-Za-z0-9_]
#   \W  匹配非字母字符，即匹配特殊字符
#   \A  仅匹配字符串开头,同^
#   \Z  仅匹配字符串结尾，同$
#   \b  匹配\w和\W之间，即匹配单词边界匹配一个单词边界，也就是指单词和空格间的位置。
#       例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
#   \B  [^\b]




# re的方法
#re.findall()返回列表
s=re.findall('\d+','a1515ds51a3dw15wfad6vb1ad6w5')
print(s)

#re.fubditer()返回迭代器
s=re.finditer('\d+','a1515ds51a3dw15wfad6vb1ad6w5')
print(next(s).group())
print(next(s).group())

#.search 只匹配第一个结果,返回对象,的位置和长度,和信息,失败返回None
#group()获取信息
#span() 获取位置
ret=re.search('\d+','a1515ds51a3dw15wfad6vb1ad6w5')
print(ret.span())
print(ret.group())

#match:之在字符串开始的位置匹配
ret=re.match('\d+','1515ds51a3dw15wfad6vb1ad6w5')
print(ret.group())

#split('规则','分割字符串',[次数])按规则分割
s=re.split('\d+','1515ds51a3dw15wfad6vb1ad6w5')
print(s)

#sub('规则','替换付','替换字符串',[次数])
s=re.sub('\d+','AAA','hello 324sdf35')
print(s)

#compile 先设定规则,在后再执行
c=re.compile('\d+')
s=c.findall('hello32world45')
print(s)


#命名分组
res=re.search(r"(?P<author>\w+)+\.aticles\.(?P<id>\d{4})","yuan.aticles.1234")
print(res.group('author'))
print(res.group('id'))

#重复
print(re.findall('\d{4}','sd5348fsdv2147sdfasd554asdfa333'))

#非贪婪匹配 将每个字符分开匹配
print(re.findall('\d+?','sd5348fsdv2147sdfasd554asdfa333'))
print(re.findall('(sd\d+)?','sd5348fsdv2147sdfasd554asdfa333'))

#计算 "1 - 2 * ( (60-30+(-40/5) * (9-2*5/3 + 7 /3*94/4*2998 + 10 * 568/14))- (-4*3)/ (16-3*2) )"
s="1 - 2 * ( (60-30+(-40/5) * (9-2*5/3 + 7 /3*94/4*2998 + 10 * 568/14))- (-4*3)/ (16-3*2) )"
res=re.search(r'\([^()]+\)',s)
print(res.group())
print(eval(res.group()))
#   ^       以什么开头
#   $       以什么结尾
#   .       任意1个字符
#   \       转移字符如:  a\\  匹配a\
#   ?       0或1个前一字符
#   *       代表>=0个任意字符
#   +       前1个字符匹配1次或无限次
#   {m}     匹配m次
#   {m,n}   匹配m到n次
#   {a,b}   最少a个,最多b个
#   [abef]  其中一个字符
#   \d      [0-9]任意数字
#   \s      空白字符:空格、换行等
#   \S      非空白字符
#   \w      单词字符[a-zA-Z0-9]
#   \W      非单词字符

import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

print("matchObj.group(2)" , matchObj.group())
print(re.search('www', 'www.runoob.com.www').span())



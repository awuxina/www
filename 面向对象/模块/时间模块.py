import time
print('返回当前时间的时间戳:',time.time())     #返回当前时间的时间戳,从1970:00:00 到现在的秒

print('按特定格式返回时间:',time.strftime('%Y-%m-%d %X'))

t=time.localtime()     #返回当地格式的时间 tm_wday星期几  tm_yday今年对的几天
print('年',t.tm_year)
print('月',t.tm_mon)
print('日',t.tm_mday)
print('时',t.tm_hour)
print('分',t.tm_min)
print('秒',t.tm_sec)
print('星期几',t.tm_wday+1)  #这是从0开始
print('今年第',t.tm_yday,'天')
print(t.tm_isdst)   #不知道

c=time.localtime(time.time())   #将时间戳转换成本地时间
print(time.gmtime())

#时间戳<----->结构化时间
print('time.localtime==',time.localtime(3600*24))
print('time.gmtime==',time.gmtime(3600*24))    #世界标准时间
print('time.mktime==',time.mktime(time.localtime(3600*24)))


#时间戳<---->结构化时间
print('time.strftime==',time.strftime('%Y-%m-%d %X',time.localtime()))
print('time.strptime==',time.strptime("2018-2-23","%Y-%m-%d"))


print(time.ctime(time.time()))
print(time.asctime(t))

time.sleep(5)#线程推迟5秒运行
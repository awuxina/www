#super().__init__()     #调的父类绑定方法
#.__bases__             #查看父类
#对象.__class__         #查看产生类
#对象.moudule__         #查看模块名
#类.mro()               #查看继承顺序
# raise AttributeError  #抛出异常
# eval('print("aaaa")') #将字符串转为代码
# print(abs(-1))          #求绝对值
# print(all((1,2)))       #是否是可迭代对象,是返回True
# print(any(()))          #可跌代对象为空,返回False
# print(sum((1,2,3,4,5))) #计算sum的和
# print(bool(0))          #0 None ''则为False
# print(bytes('hello',encoding='utf-8'))      #转换成字节格式
# print(bin(10))          #转换为二进制
# print(hex(10))          #转换为16进制
# print(oct(10))          #转换为8进制
# def test():pass
# print(callable(test))   #是否可以被调用,可以返回True
# print(chr(60))          #ASCII码和数字互相转换
# print(isinstance(1,int))#判断参数1数不是参数2的类型,是返回True
# f=frozenset({1,2,3,4})  #不可变集合
# print(dir(int))         #dir查看里面的方法
# print(divmod(10,3))     #10/3返回(3,1)
# for i in enumerate([1,2,3,4]):      #取出值的索引和元素
#     print(i)
# print(globals())        #看全部变量
# print(hash('asdf'))     #获得数据哈希值,较验数据完整性
# print(id('sadf'))       #查看数据身份
# print(pow(3,2))         #3的2次方
# print(pow(3,2,2))       #3的2次方,再对2取余
# print(list(reversed([1,2,3,4,5])))      #反转数据变成1个可迭代对象
# print(round(10.3))      #四舍六入,留双
#print(hasattr(p,'name'))#查找p对象下,是否有'name'这个属性
#print(callable(p))      #查看p是不是可调用对象

#slice
# l=[i for i in range(1,6)]
# print(l[2:5])
# s=slice(2,5)
# print(l[s])
#slice  END

# print(vars() is locals())
#
# m=__import__('time')        #将字符串当1个模块导入
# m.sleep(3)
# import time
# print(time.localtime())         #当前时间
# print(time.localtime(time.time()+86400))   #明天的时间
#拉链
# l1=[1,2,3]
# s='hel'
# for i in zip(l1,s):
#     print(i)
#拉链 END

l=[3,4,1,0,9,10]
# print(sorted(l))        #将对象以升序排序,返回值是列表
# print(sorted(l,reverse=True))        #将对象以降序排序,返回值是列表

# #找出工资最高的人 同理min
salaries={
    'egon':3000,
    'alex':100000,
    'lisi':200
}
# def get_value(k):
#     return salaries[k]
# print(max(salaries,key=get_value))
#
# #匿名函数
# # f=lambda k:salaries[k]
# print(max(salaries,key=lambda k:salaries[k]))
# #找出工资最高的人   END
#按工资排序,得到名字列表
# print(sorted(salaries,key=lambda k:salaries[k]))#升序
# print(sorted(salaries,reverse=True,key=lambda k:salaries[k]))#降序


#map:映射
# l=[1,2,3,7,5]
# m=map(lambda item:item**2,l)
# print(list(m))
#
# name_l=['alex','zhengsan','lisi','wangwu']
# m=map(lambda name:name+'SB',name_l)
# print(list(m))
#map    END

#reduce:合并
# from functools import reduce
# l=range(100)
# res=reduce(lambda x,y:x+y,l)
# print(res)
# res=reduce(lambda x,y:x+y,l,100)
# print(res)
#reduce END

#filter:过滤
name_l=[
    {'name':'egon','age':18},
    {'name':'dragonFire','age':1000},
    {'name':'gaoluchuan','age':9000},
    {'name':'fsw','age':10000},
]
res=filter(lambda d:d['age']>100,name_l)
# for i in res:
    # print(i)
#filter END


# import os
# os.wait('c:\egon') #找到c:\egon 下的所有文件和文件夹

#抽象类
# import abc
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def run(self):
#         pass
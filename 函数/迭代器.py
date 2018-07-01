#可迭代的:对象本身内置__iter__方法,那就是可迭代的
#可迭代对象有__next__方法,可用于取值
# d={'a':1,'b':2,'c':3}
# d.__iter__()# 等同 iter(d)
# i=d.__iter__()
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
#可迭代的:对象本身内置__iter__方法,那就是可迭代的  END

#for循环的原理
d={'a':1,'b':2,'c':3}
i=iter(d)
while True:
    try:
        print(next(i))
    except StopIteration:
        break
#for循环的原理   END

#为什么用迭代器
    #优点:
        #1:迭代器提供了一种不依赖索引的取值方式,这样可以遍历没有索引的对象(字典、集合、文件)
        #2迭代器与列表比较,迭代器是惰性计算的,更节省内存

    #缺点:
        #1:迭代器无法获取长度,使用不如列表灵活
        #2:一次性的,只能往后取值,不能回头

#查看可迭代对象
from collections import Iterable,Iterator
s='hell'
l=[1,2,3]
t=(1,2,3)
d={'a':1}
set1={1,2,3,4}
f=open('../语言基础/text2.txt')

#都是可迭代的
s.__iter__()
l.__iter__()
t.__iter__()
d.__iter__()
set1.__iter__()
f.__iter__()

print(isinstance(s,Iterable))#s是不是Iterable对象
print(isinstance(l,Iterable))
print(isinstance(t,Iterable))
print(isinstance(d,Iterable))
print(isinstance(set1,Iterable))
print(isinstance(f,Iterable))
#都是可迭代的 END

#查看是否是迭代器
print(isinstance(s,Iterator))#s是不是Iterator(迭代器)对象
print(isinstance(l,Iterator))
print(isinstance(t,Iterator))
print(isinstance(d,Iterator))
print(isinstance(set1,Iterator))
print(isinstance(f,Iterator))
#查看是否是迭代器   END
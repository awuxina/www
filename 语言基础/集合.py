#求交集
# linux = ['alex','jack','rain','sb']
# python = ['sb','alex','mack','rachel']
# result = []
# for i in python:
#     if i in linux:
#         result.append(i)
# print(result)
#求交集    END


linux = {'alex','jack','rain','sb','alex'}
python = {'sb','alex','mack','rachel'}
result = {}
a = {'sb'}
#集合天然去重
# print(linux)

#交集
#result = linux.intersection(python)#简写 print(linux & python)

#差集 linux有 但python没有
#result = linux.difference(python)  #简写 print(linux - python)

#并集
#result = linux.union(python)        #简写 print(linux | python)

#反向差集 互相没有的数据
#result =linux.symmetric_difference(python)  #简写print(linux ^ python)
print(result)

#集合合并
# linux.update(python)#相当把python直接合并linux中

# 判断python是否是linux子集
#print(linux.issubset(python))

#父集
#print(linux.issuperset(a))

#两个集合交集为空则返回真
#print(linux.isdisjoint(python))

#增加
#linux.add('a')

#取出差集再存入linux
#linux.difference_update(python)

#删除
#linux.discard('sb')

#删除,但元素不存在会报错
#linux.remove("dd")

#随机删除1个
#linux.pop()


print(linux)



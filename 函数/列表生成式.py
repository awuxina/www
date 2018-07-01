'生成100个列表'
#方法 1
egg_list=[]
for i in range(100):
    egg_list.append('egg{i}'.format(i=i))
#方法1    END

#方法2
l=['egg{i}'.format(i=i) for i in range(100) if i>50]
#print(l)
#方法 2   END

l=[1,2,3,4]
s='hello'
l1=[(num,s1) for num in l for s1 in s]
#print(l1)

l=[1,2,3,4]
s='hello'
l1=[(num,s1) for num in l if num>2 for s1 in s]
#print(l1)


import os
g=os.walk('egon')
path=['路径:{i}{j}'.format(i=i[0],j=j) for i in g for j in i[-1]]
print(path)
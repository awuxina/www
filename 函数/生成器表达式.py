
l=['egg{i}'.format(i=i) for i in range(100)]
print(l)

g=l=('egg{i}'.format(i=i) for i in range(100))
print(g)
print(next(g))
print(next(g))

g=('egg{i}'.format(i=i) for i in range(100))
list=list(g)
print(list)

g=(i for i in range(101))
nums_g=(i for i in g)
print(sum(nums_g))


'计算b.txt 使用的价格'
money_l=[]
with open('b.txt') as f:
    for line in f:
        goods=line.split()
        res=float(goods[-1])*float(goods[-2])
        money_l.append(res)
print(money_l)
print(sum(money_l))

f=open('b.txt')
g=(float(line.split()[-1])*float(line.split()[-2]) for line in f)
print(sum(g))
f.close()

'读取字典'
res=[]
with open('b.txt') as f:
    for i in f:
        goods=i.split()
        res.append({'name':goods[0],'price':goods[1],'num':goods[2]})
print(res)

f=open('b.txt')

dic_g=({'name':i.split()[0],'price':i.split()[1],'num':i.split()[2]} for i in f)
print(dic_g)
for i in dic_g:
    print(i)
f.close()
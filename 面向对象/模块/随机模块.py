import random
print('random.random====>',random.random())  #0--1的浮点数字
print('random.randint====>',random.randint(1,100))  #>=1,<=100整数
print('random.randrange====>',random.randrange(0,100))  #>=1,<100整数
print('random.choice====>',random.choice([1,5,9,6,22,66]))   #随机取1个
print('random.sample====>',random.sample([1,5,9,6,22,66],2)) #随机取2个,不可重复
print('random.uniform====>',random.uniform(1,3))  #>1,<3小数

#随机排序
item=[1,3,5,7,9]
random.shuffle(item)
print('random.shuffle====>',item)


#获取5位一验证码
def validate():
    l=['a','b','c','d','f','g','h','i','啊','哦','好','坏']
    list=''
    i=0
    while i<5:
        res=random.choice(l)
        list+=res
        i+=1
    return list
print(validate())
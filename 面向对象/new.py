#python中:
#属性:特征(变量)和技能(函数、绑定方法)
#类.xxxxx xxxxx可能是属性也可能是方法
#__init__(self) init是初始化方法,self代表本类
#类.__dict__ 查看类的名称空间
#对象.__dict__ 查看对象的名称空间

#定义学生类
# 特征:共同国籍'china'
# 技能:查看成绩
class Student:
    country='China'
    def __init__(self,ID,NAME,SEX,PROVINCE):
        self.id=ID
        self.name=NAME
        self.sex=SEX
        self.province=PROVINCE

    def search_score(self):
        print('tell score')

#类的用法:实例化,属性引用
s1=Student('01','cobila','female','shanxi')
s1.search_score()
# print(s1.name)
# print(Student.__dict__)
# print(s1.__dict__)

class Riven:
    camp='Noxus'#玩家的英雄(锐雯)的阵营noxus
    def __init__(self,nickname,aggressivity=54,life_value=414):#初始攻击54
        self.nickname=nickname  #玩家名字
        self.aggressivity=aggressivity  #初始攻击力
        self.life_value=life_value  #生命值
    def attack(self,enemy):#普通攻击技能, enemy是敌人
        enemy.life_value -= self.aggressivity

class Garen:
    camp='Noxus'#玩家的英雄(锐雯)的阵营noxus
    def __init__(self,nickname,aggressivity=60,life_value=500):
        self.nickname=nickname  #玩家名字
        self.aggressivity=aggressivity  #初始攻击力
        self.life_value=life_value  #生命值
    def attack(self,enemy):#普通攻击技能, enemy是敌人
        enemy.life_value-=self.aggressivity

r=Riven('瑞雯雯')
g=Garen('草丛轮')
g.attack(r)
print(r.life_value)
#多态(定义角度) :同一种事物的多种形态,动物分,人类,猪类,狗类
class Aniaml:#动物类
    def run(self):
        print('动物在走')

class People(Aniaml):#人类
    def run(self):
        print('人在走')
class Pig(Aniaml):#猪类
    def run(self):
        print('猪在走')
class Dog(Aniaml):#狗类
    def run(self):
        print('狗在走')

peo=People()
pig=Pig()
peo.run()
pig.run()

#多态性(使用角度):
    #1.继承
    #2.
#定义统一的接口,可以传入不同类型的值,但调用逻辑一样,执行结果不一样
def fun(obj):
    obj.run() #调用的不同类的同一种发方法

fun(pig)

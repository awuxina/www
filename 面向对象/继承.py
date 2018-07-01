# class ParentClass1:#定义父类
#     pass
#
# class ParentClass2:#定义父类
#     pass
#
# class SubClass1(ParentClass1):#继承ParentClass1
#     pass
#
# class SubClass2(ParentClass2):#继承ParentClass2
#     pass
#
# print(ParentClass1.__bases__)#查看父类
# print(SubClass1.__bases__)
# print(SubClass2.__bases__)

class Aniaml:#动物类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def walk(self):
        print('{name} 正在走路'.format(name=self.name))

    def say(self):
        print('{name} 正在叫'.format(name=self.name))

class People(Aniaml):#人类
    #添加特有的属性
    def __init__(self,name,age,ear):
        Aniaml.__init__(self,name,age)
        self.ear=ear
    def walk(self):
        #重写父类方法
        print('{name} 正在慢慢走路'.format(name=self.name))

class Pig(Aniaml):#猪类
    def walk(self):
        #继承父类方法,添加新属性
        Aniaml.walk(self)
        print('猪不会走,只会跑')

class Dog(Aniaml):#狗类
    pass

p1=People('奥巴马',50,'小耳朵')
print(p1.name,p1.age,'岁',p1.ear)
p1.walk()

pig=Pig('小猪',3)
pig.walk()
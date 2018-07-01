#把对象模拟成字典操作
class Foo:
    # __slots__ = ['x']# 设置应该有的属性,再不能在类外设置属性
    def __init__(self,name):
        self.name=name

    def __getitem__(self, item):
        print('getattr')
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key]=value

    def __delitem__(self, key):
        print('del obj[key]时,我执行')
        self.__dict__.pop(key)



f=Foo('egon')
print(f.name)

#设置item后
f['age']=18
print(f.age)

del f['age']
# print(f.age)


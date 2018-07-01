class People:
    country='China'
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(self.country,self.name)
p=People('egon')

# print(hasattr(p,'name'))#查找p对象下,是否有'name'这个属性
# print(getattr(p,'country'))#找到p对象下的country并执行
#
# f=getattr(p,'walk')#t=p.walk
# print(f)
#
# f1=getattr(People,'walk')
# print(f1)
#
# print(getattr(f,'walk11','这个属性不存在'))

# if hasattr(p,'walk'):
#     func=getattr(p,'walk')
#     func()
# print('====>')

#setattr()的运用
p.sex='男'
print(p.sex)
print(p.__dict__)

setattr(p,'age','123')
print(p.__dict__)

#delattr()删除
delattr(p,'age')
print(p.__dict__)

import sys
this_module=sys.modules[__name__]   #在导入__name__模块
print(this_module)
print(hasattr(this_module,'p'))
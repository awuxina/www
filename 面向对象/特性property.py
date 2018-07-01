#@porperty 将技能改变成属性使用
#被property装饰的属性会优先于对象的属性被使用
#而被property装饰的属性分三种:
    #1.property
    #2.sex.setter
    #3.sex.deleter
import math#数学包
class Circle:#圆
    def __init__(self,radius):  #圆半径
        self.radius=radius

    @property   #area=property(area)
    def area(self):
        return math.pi * self.radius**2 #计算面积
    @property #perimeter=property(perimeter)
    def perimeter(self):
        return 2*math.pi * self.radius  #计算周长

c=Circle(7)
print('半径',c.radius)
print('面积',c.area)
print('周长',c.perimeter)


# class People:
#     BMI=''
#     def __init__(self,name,age,height,weight):#height厘米  weight公斤
#         self.name=name
#         self.age=age
#         self.height=height/100
#         self.weight=weight
#
#     @property
#     def body_index(self):
#         return self.weight/(self.height**2)
#
#     @property
#     def body_status(self):
#         status = ''
#         if self.body_index <= 18.4:
#             status = '偏瘦'
#         elif self.body_index >= 18.5 and self.body_index <= 23.9:
#             status = '正常'
#         elif self.body_index >= 24 and self.body_index <= 27.9:
#             status = '过重'
#         else:
#             status = '肥胖'
#         return status
#
# def weight_distance(obj):
#     weight=obj.body_index*obj.height**2
#     #偏瘦体重
#     weight_small=18.5*obj.height**2
#     #正常体重
#     weight_normal=24*obj.height**2
#     #偏重体重
#     weight_ageain = round(28 * obj.height ** 2,2)
#     print('距离偏重体重:',round(weight-weight_ageain,2),'斤')
#     print('距离正常体重:',round(weight-weight_normal,2),'斤')
#     print('距离偏瘦体重:',round(weight-weight_small,2),'斤')
#
# p=People('兰涛',32,165,101)
# print(p.body_index)
# print(p.body_status)
# weight_distance(p)

#get set
class People:
    def __init__(self,name,SEX):
        self.name=name
        # self.__sex=SEX
        self.sex=SEX
    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self,value):
        if not isinstance(value,str):
            raise TypeError('性别必须是字符串类型')
        self.__sex=value

    @sex.deleter
    def sex(self):
        del self.__sex
p=People('李四','男')
# p=People('李四',141)
print(p.name,p.sex)
p.sex='女'
print(p.name,p.sex)
print(p.sex)
# del p.sex     #删除sex属性
# print(p.sex)
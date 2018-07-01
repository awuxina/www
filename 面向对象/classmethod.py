# class Foo:
#     @classmethod #把一个方法绑定给类:类.绑定到类的方法(),会把类本身当做第一个参数自动传给后面的方法
#     def test(cls,x):
#         print(cls,x)
#
#     def bar(self):
#         pass
# # f=Foo()
# # f.test()
#
# Foo.test(123)

#__str__ 定义类在内部,必须反悔一个字符串类型,
#什么时候执行?打印这个类产生的对象时,会触发执行
class People:
    a='aa'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return '{name}你好啊!{age}岁'.format(name=self.name,age=self.age)
p=People('egon',18)
print(p)
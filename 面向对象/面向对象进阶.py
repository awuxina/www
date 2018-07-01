class Fo:
    pass
class Foo(Fo):
    pass

obj=Foo()

print(isinstance(obj,Foo))# obj是否是Foo类
print(issubclass(Foo,Fo)) #Foo是不是Fo的派生类
print(Foo.__bases__)    #查看Foo的父类

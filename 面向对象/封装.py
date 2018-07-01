#__名字,这种语法,只在定义的时候才有变形效果,如果类或对象已经产生,就不会有变形效果
#内部能够self.__名字访问
class A:
    __x=1   #变成了:_A__x
    def test(self):
        print('A')

    def __test(self):#_A__text
        print('__A')

# print(A.__x)
# A.test(11)

a=A()
a.y=1
print(a.y)
a.test()

print(A.__dict__)
#@staticmethod 取消方法的self 传值
# class Foo:
#     def spam(self):
#         print('---->',self)
#
# Foo.spam(123132)

class Foo:
    @staticmethod
    def spam(x,y,z):
        print(x,y,z)
Foo.spam(1,2,3)

f=Foo
f.spam(1,2,3)
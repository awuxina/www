class Foo:
    x=1
    def run(self):
        pass

def run(self):
    print('')
#创建类过程
class_name='Bar'#创建类名
class_dic={ #创建命名空间
    'x':1,
    'run':run
}
bases=(object,)#类继承关系
Bar=type(class_name,bases,class_dic)#类的实例化
print(Bar)
#创建类过程  END

s=type('Spam',(),{})
print(s)
print(s.__bases__)
print(s.__dict__)
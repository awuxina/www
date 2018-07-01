# 元类就是深度的魔法,
# 99%的用户应该根本不必为此操心.
# 如果你想搞清楚究竟是否需要用到元类,那么你就不需要它.
# 那些实际用到元类的人都非常清楚地知道他们需要做什么,
# 而且根本不需要及解释为什么要用元类
class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        print(class_name)
        print(class_bases)
        print(class_dic)
        type.__init__(self,class_name,class_bases,class_dic)#可不写,系统默认添加
        for key in class_dic:
            if not callable(class_dic[key]):continue
            if not class_dic[key].__doc__:
                raise TypeError('请写备注')

    def __call__(self, *args, **kwargs):
        print(self)
class Foo(metaclass=Mymeta):#指定元类,默认type
    x=1
    def run(self):
        '备注'
        print('running')

# type('Foo',(object,),{'x':1,'run':run})
# Foo=Mymeta('Foo',(object,),{'x':1,'run':run}
f=Foo()

class Mymeta1(type):
    def __init__(self, class_name, class_bases, class_dic):
        pass

    def __call__(self, *args, **kwargs):
        print(self)
        obj=self.__new__(self)#空对象
        self.__init__(obj, *args, **kwargs)
        return obj
class Fa(metaclass=Mymeta1):
    x=1
    def __init__(self,name):
        self.name=name
    def run(self):
        print('running')

fa=Fa('egon')
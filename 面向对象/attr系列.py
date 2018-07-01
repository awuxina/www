class Foo:
    def __init__(self,name):
        self.name=name

    def __setattr__(self, key, value):
        # print('------setattr-----key:{key}-----value:{value}'.format(key=key,value=value))
        #设置类型限制
        # if not isinstance(value,str):
        #     raise TypeError('must be str')
        self.__dict__[key]=value

    def __delattr__(self, item):
        print('delattr:{item}'.format(item=item),type(item))

    #属性不存在的情况下触发
    def __getattr__(self, item):
        print('getattr----->{item}'.format(item=item))
f=Foo('egon')
f.age=18
print(f.__dict__)
del f.age
a=f.age
print()
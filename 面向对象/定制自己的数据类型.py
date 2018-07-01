#定制一个只能添加int类型的列表
class List(list):
    def append(self, p_object):
        # print('---->',p_object)
        if isinstance(p_object,int):
            super().append(p_object)
        else:
            raise TypeError('must be int')

    def insert(self, index: int, object: object):
        if isinstance(object,int):
            super().insert(index,object)
        else:
            raise TypeError('must be int')

    def __setattr__(self, key, value):#设置属性的时候调用
        pass

    def __getattr__(self, item):#属性不存在时调用
        pass

    def __delattr__(self, item):#删除属性时调用
        pass
l=List([1,2,3])
l.append(4)
print(l)

l.insert(0,9)
print(l)
class Open:
    def __init__(self,filepath,mode='r',encode='utf-8'):
        self.f=open(filepath,mode=mode,encoding=encode)

    def write(self):
        pass

    def __getattr__(self, item):
        return getattr(self.f,item)

    #析构函数,该类的对象在删除时执行
    def __del__(self):
        print('----->del')
        self.f.close()

f=Open('a.txt','w')
print('======>')
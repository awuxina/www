class Foo:
    def __enter__(self):#with 时执行__enter__方法
        print('============>enter')
        return '1'

    def __exit__(self, exc_type, exc_val, exc_tb):#with代码抛出异常结束时结束后执行
        print('============>exit')
        print('exc_type:',exc_type)
        print('exc_val:',exc_val)
        print('exc_tb:',exc_tb)
        print('============>exit    END')
        return True

with Foo() as object:
    print('with foo的自代码块,{obj}'.format(obj=object))
    raise NameError('名字没有定义')
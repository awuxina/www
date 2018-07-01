def auth2(auth_type):
    def auth(func):
        print(auth_type)
        def wrapper(*args,**kwargs):
            if auth_type=='file':
                name=input('用户名:').strip()
                pwd=input('密码:').strip()
                if name=='zhangsan' and pwd=='111111':
                    print(name,pwd)
                    func(*args,**kwargs)
            else:
                print('会不会玩')
        return wrapper
    return auth

@auth2(auth_type='file') #@auth  #index=auth(index)
def index(a):
    print('被装饰者',a)

index('222')
import time
#在不动用index的情况下 添加别的功能
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         res=func(*args,**kwargs)
#         stop=time.time()
#         print('运行时间:{time}'.format(time=start-stop))
#     return wrapper
#
# @timmer #index=#timmer(index)  #这就是装饰器  #@timmer就是把index作为1个变量赋值给timmer
# def index():
#     print('被装饰者')
#
# index()
#在不动用index的情况下 添加别的功能   END

def timmer(func):
    def wrapper(*args,**kwargs):
        print('====>',list(args))
        start=time.time()
        func(*args,**kwargs)
        time.sleep(2)
        stop=time.time()
        # print('运行时间{time}'.format(time=stop-start))
    return wrapper

@timmer
def home(name):
    print('欢迎来到home:{name}'.format(name=name))

@timmer
def auth(name,pwd):
    print(name,pwd)

home('李三')


auth('李四','123')

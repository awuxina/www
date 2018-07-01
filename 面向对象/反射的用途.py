import sys
def add():
    print('add')

def change():
    print('change')

def search():
    print('search')

def delete():
    print('delete')



#输入名称执行方法
#方法一:
# func_dic={
#     'add':add,
#     'change':change,
#     'search':search,
#     'delete':delete
# }

# while True:
#     cmd=input('>>:').strip()
#     if not cmd:continue
#     if cmd in func_dic:
#         func=func_dic.get(cmd)
#         func()

#方法二
# this_module=sys.modules[__name__]#生成相应的字典
# while True:
#     cmd=input('>>:').strip()
#     if not cmd:continue
#     if hasattr(this_module,cmd):
#         func=getattr(this_module,cmd)
#         func()
#输入名称执行方法   END

#动态导入模块
# m=input('请输入你要导入的模块:')
# m1=__import__(m)
# print(m1.time())


#官方推荐动态导入模块
import importlib
t=importlib.import_module('time')
print(t.time())

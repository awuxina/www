import os
#找到egon下所有文件的文件路径
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper

@init
def serarch(target):
    while True:
        dir_name=yield
        g=os.walk(dir_name)
        for i in g:
            for j in i[-1]:
                file_path='{i}\\{j}'.format(i=i[0],j=j)
                target.send(file_path)


@init
def opener(target):
    '打开文件'
    while True:
        file_path=yield
        with open(file_path) as f:
            target.send((file_path,f))

@init
def cat(target):
    '读取文件内容'
    while True:
        file_path,f=yield
        for line in f:
            target.send((file_path,line))

@init
def grep(pattern,target):
    '过滤一行内容中有无pattern'
    while True:
        file_path,line=yield
        if pattern in line:
            target.send(file_path)

@init
def printer():
    '打印文件路径'
    while True:
        file_path=yield
        print(file_path)

e=serarch(opener(cat(grep('python',printer()))))
e.send('egon')

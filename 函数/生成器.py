# #生成器就是一个函数,这个函数内包含yield这个关键字
# from collections import Iterator
# def test():
#     print('one')
#     yield 1 #return 1
#     print('two')
#     yield 2  # return 2
#     print('three')
#     yield 3  # return 3
#     print('four')
#     yield 4  # return 4
#
# g=test()
# # print(g)
# # print(isinstance(g,Iterator))
#
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# res=next(g)
# print(res)
# res=next(g)
# print(res)
# res=next(g)
# print(res)
# res=next(g)
# print(res)

#生成器的运用模仿CentOS tail -f
import time
def tail(file_path):
    with open(file_path,'r') as f:
        f.seek(0,2)
        while True:
            line=f.readline()
            if not line:
                time.sleep(1)
                continue
            else:
                #print(line)
                yield line
g=tail('test.txt')
for i in g:
    if 'error' in i:
        print(i)
    time.sleep(1)
#生成器的运用模仿CentOS tail -f END
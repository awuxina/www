# from collections import Iterable,Iterator
# class Foo:
#     def __init__(self,start):
#         self.start=start
#
#     def __next__(self):
#         n=self.start
#         self.start+=1
#         return self.start
#
#     def __iter__(self):
#         return self
#
# f=Foo(0)
#
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
#
# j=0
# for i in f:
#     print('======>',i)
#     j+=1
#     if j==10:
#         break


class Range:
    '123'
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start==self.end:
            raise StopIteration

        n=self.start
        self.start+=1
        return n

print(Range.__doc__)
s='hello'
try:
    int(s)
except IndexError as i:
    pass
except Exception as e:
    print(e)
else:
    print('try内代码没有异常执行')
finally:
    print('无论是否异常,都会执行该代码块,通常清理操作')

try:
    raise IndexError('主动触发异常')
except IndexError as ie:
    print(ie)

#自定义异常
class MyException(BaseException):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

try:
    raise MyException('自定义异常')
except MyException as e:
    print(e)

#断言
x=1
y=1
assert x==y
print('===>')
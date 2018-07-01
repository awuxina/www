"""
协成优点:
    1.单线程,不能再切换
    2.不再有任何锁的概念
"""
import time

def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('n=====>')
        time.sleep(1)
        r='200 OK'

def produce(c):
    next(c)
    n=0
    while n<5:
        n=n+1
        cr=c.send(n)
        print('cr====>',cr)

    c.close()

if __name__ == '__main__':
    c=consumer()
    produce(c)
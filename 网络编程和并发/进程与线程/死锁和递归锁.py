import threading
import time

# mutex_a=threading.Lock()
# mutex_b=threading.Lock()

Rlock=threading.RLock()

class MyThreading(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):
        # mutex_a.acquire()
        Rlock.acquire() #count=1
        print('I am {name},get res:{time}'.format(name=self.name,time=time.time()))
        # mutex_b.acquire()
        Rlock.acquire() #count=2
        # mutex_b.release()
        Rlock.release() #count=1
        # mutex_a.release()
        Rlock.release() #count=0

    def fun2(self):
        # mutex_b.acquire()
        Rlock.acquire()

        print('I am {name},get res:{time}'.format(name=self.name, time=time.time()))
        # time.sleep(0.2)

        # mutex_a.acquire()
        Rlock.acquire()
        print('I am {name},get res:{time}'.format(name=self.name, time=time.time()))
        # mutex_a.release()
        Rlock.release()
        # mutex_b.release()
        Rlock.release()

if __name__=='__main__':
    print('start-----------------------{time}'.format(time=time.time()))
    for i in range(0,10):
        my_thread=MyThreading()
        my_thread.start()
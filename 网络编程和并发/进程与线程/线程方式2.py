import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        print('线程开启======>{num}'.format(num=self.num))


t1 = MyThread(56)
t2 = MyThread(78)
t1.start()
t2.start()
t1.join()
t2.join()
print('结束')

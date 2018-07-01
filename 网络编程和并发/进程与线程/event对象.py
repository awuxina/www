#event.wait() 程序将会阻塞,直到别的程序调用event.set()时,才继续乡下执行
#event.isSet():返回event的状态值
#event.wait():如果event.isset()==False将阻塞线程
# event.set():设置event的状态值为True,将所有阻塞池激活,等待操作
# event.clear():恢复event的状态值为False

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format='%(threadName)-10s) %(message)s',)

def worker(event):
    logging.debug('waiting fro redis ready...')
    while not event.isSet():
        event.wait(1)
        logging.debug('wait....')
    logging.debug('redis ready,and connnect to redis server and do some work {time}'.format(time=time.time()))
    time.sleep(1)

def main():
    readis_ready = threading.Event()
    t1=threading.Thread(target=worker,args=(readis_ready,),name='t1')
    t1.start()

    t2 = threading.Thread(target=worker, args=(readis_ready,), name='t2')
    t2.start()

    logging.debug('first of all, check redis server, make sure itis OK, and then trigger the')
    time.sleep(6)
    readis_ready.set()

if __name__ == '__main__':
    main()


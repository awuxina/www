import time
import threading

def subNum():
    global num  #每个线程中都获取这个全局变量
    lock.acquire()#锁定
    temp = num
    time.sleep(0.0000001)
    num=temp-1
    lock.release()#解锁

num=100

lock=threading.Lock()#创建同步锁

thread_list=[]
for i in range(100):
    t=threading.Thread(target=subNum)
    t.start()
    thread_list.append(t)

# for i in thread_list:#等待所有线程执行完毕
#     t.join()

print('Result:',num)
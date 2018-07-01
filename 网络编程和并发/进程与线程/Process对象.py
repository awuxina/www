""""
multiprocessing.Process对象 是进程对象
is_alive():返回进程是否在运行
join([timeout]):阻塞当前环境下的进程,知道调用次方法的进程终止或到达指定的timeout
start():进程准备就绪,等待CPU调度
run():start()调用run()方法,如果实例进程使未制定传入target,这star执行默认run()方法
terminate():不管任务是否完成,立即停止工作进程
属性:
daemon:和线程的setDeamon功能一样
name:进程名字
pid:进程号
"""
from multiprocessing import Process
import time
class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        print('hello',self.name,time.ctime())
        time.sleep(1)

if __name__=='__main__':
    p_list=[]
    for i in range(3):
        p=MyProcess()
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    print('end')
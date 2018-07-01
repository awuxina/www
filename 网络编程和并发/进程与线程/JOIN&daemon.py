# Thread实例对象的方法
  # isAlive(): 返回线程是否活动的。
  # getName(): 返回线程名。
  # setName(): 设置线程名。
# threading模块提供的一些方法：
  # threading.currentThread(): 返回当前的线程变量。
  # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
  # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

"""
总结:对于密集型任务:python的多线程并没有用
总结:对于IO密集型任务:python的多线程有意义
"""
import threading
from time import ctime,sleep

def music(name):
    print('Begin music to {name}. {time}'.format(name=name,time=ctime()))
    sleep(3)
    print('end music time:{time}'.format(time=ctime()))

def blog(title):
    print('Begin blog the {title}. {time}'.format(title=title,time=ctime()))
    sleep(5)
    print('end blog time:{time}'.format(time=ctime()))

threads=[]

t1=threading.Thread(target=music,args=('FILL ME',),name='sub_thread')
t2=threading.Thread(target=blog,args=('python',))
threads.append(t1)
threads.append(t2)

if __name__=='__main__':
    #设置守护线程 当主线程结束时,子线程如果没有执行完会强制结束
    t1.setDaemon(True)
    # t2.setDaemon(True)
    # 设置守护线程    END
    for t in threads:
        t.start()

    # t2.join()#等待线程t2
    print('all over {time}'.format(time=ctime()))
import threading
import time
def songs():
    print('听歌')
    time.sleep(3)
    print('听歌结束')

def blogs():
    print('写博客')
    time.sleep(5)
    print('写博客结束')

start=time.time()
#单线程
# songs()
# blogs()


t1=threading.Thread(target=songs)
t2=threading.Thread(target=blogs)
t1.start()#线程开始
t2.start()#线程开始
t1.join()#等待线程
t2.join()#等待线程
end=time.time()
print('用时:',end-start)
#管道 优点: 线程安全的
import  queue
# q=queue.Queue(3)#先进先出3个数据的管道
q=queue.LifoQueue()#先进后出
q.put(11)
q.put("hello")
q.put(222)
q.put(333,False)#如果满了就不堵塞


print(q.get())
print(q.get())
print(q.get())

#join和task_done
q=queue.Queue(5)
q.put(111)
q.put(222)

q.get()
q.task_done()
q.get()
q.task_done()
q.join()#只有task_done()完成了才会 继续运行
print('ending')

# 优先级
q=queue.PriorityQueue()
q.put([1,'hello'])
q.put([4,'hello  4444'])
q.put([3,'hello  3333'])
print(q.get())
print(q.get())
print(q.get())

"""
q.qsize() 返回队列的大小
q.empty() 如果队列为空，返回True,反之False
q.full() 如果队列满了，返回True,反之False
q.full 与 maxsize 大小对应
q.get([block[, timeout]]) 获取队列，timeout等待时间
q.get_nowait() 相当q.get(False)非阻塞 
q.put(item) 写入队列，timeout等待时间
q.put_nowait(item) 相当q.put(item, False)
q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
q.join() 实际上意味着等到队列为空，再执行别的操作
"""
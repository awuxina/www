import time
from concurrent.futures import ThreadPoolExecutor

def task(i):
    time.sleep(1)
    print(i)

p = ThreadPoolExecutor(10)
for row in range(100):
    p.submit(task,row)
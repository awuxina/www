import time
from concurrent.futures import ProcessPoolExecutor

def task(i):
    time.sleep(1)
    print(i)

p = ProcessPoolExecutor(10)
for row in range(100):
    p.submit(task,row)
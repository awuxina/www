from gevent import monkey
monkey.patch_all()#指的是在运行时动态替换
import gevent
from urllib import request
import time

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

start=time.time()

gevent.joinall([
        gevent.spawn(f, 'https://itk.org/'),
        gevent.spawn(f, 'https://www.github.com/'),
        gevent.spawn(f, 'https://zhihu.com/'),
])
print(time.time()-start)
import urllib.request
import gevent


from  gevent import monkey
#把当前程序的所有的IO操作给我单独的做上标记
gevent.monkey.patch_all()
def f(url):
    print('GET: %s' % url)

    resp = urllib.request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data),url))

#gevent 检测不到 urllib 的io 所以就是串行了
#gevent.monkey.patch_all() 使用这个 做成并行
gevent.joinall([
    gevent.spawn(f,'https://www.python.org'),
    gevent.spawn(f,'https://www.baidu.com'),
])
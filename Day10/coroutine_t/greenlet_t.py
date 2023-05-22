import greenlet


# pip  install  gevent -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
# greenlet 是封装好的协程


def test1():
    print(12)
    gr2.switch()
    print(35)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)
    gr1.switch()

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
gr1.switch() #这里就是手动切换  相当于 yield 的next  gevent是自动切换， greenlet是手动切换


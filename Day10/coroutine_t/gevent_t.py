import gevent
#gevent 是一个第三方库，可以轻松通过gevent 实现并发同步或异步编程，在gevent中 用到的主要模式是Greenlet，它是C扩展模块形式
#接入python的轻量级协程，Greenlet 全部运行在主程序操作系统进程的内部，但它们被协作式的调度

def foo():
    print('Running in foo')
    gevent.sleep(2)
    print("Explicit context switch to foo again")

def bar():
    print('Explicit context to bar')
    gevent.sleep(1)
    print("Implicit context switch back to bar")

gevent.joinall([
    gevent.spawn(foo), #生成一个协程
    gevent.spawn(bar)
])
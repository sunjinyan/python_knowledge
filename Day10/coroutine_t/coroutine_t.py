'''
1、协程：
    单线程实现并发
    在应用程序里控制多个任务的切换+保存状态
    优点：
        应用程序级别速度要远远高于操作系统的切换
    缺点：
        多个任务一旦有一个阻塞没有切，整个线程都阻塞在原地
        该线程内的其他的任务都不能执行了

        一旦引入协程，就需要检测单线程下所有的IO行为,
        实现遇到IO就切换,少一个都不行，以为一旦一个任务阻塞了，整个线程就阻塞了，
        其他的任务即便是可以计算，但是也无法运行了

2、协程序的目的：
    想要在单线程下实现并发
    并发指的是多个任务看起来是同时运行的
    并发=切换+保存状态

优点：
无需线程上下文切换
无需原子操作锁定及同步的开销(改一个变量就是原子操作，线程需要锁，协程不需要，协程是一个线程操作)
方便切换控制流，简化编程模型
高并发+高扩展性+低成本：一个CPU支持上万的协程都不是问题，所以很适合用于高并发

缺点：
无法利用多核资源： 协程的本质是个单线程，它不能同时将单个CPU的多个核用上，协程需要和进程配合才能运行在多CPU上
当然我们日常的大部分应用都没有这个必要，除非CPU密集型操作

运行阻塞(Blocking) 操作(如IO操作)会阻塞掉整个程序
'''

def consumer(name):
    print("--->starting eating baozi...")

    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name,new_baozi))

def producer():
    r = con.__next__()
    r = con2.__next__()


    n = 0
    while n < 5 :
        n += 1
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == "__main__":
    con = consumer('c1')
    con2 = consumer('c2')

    p = producer()

def home():
    print("in func 1")

def bbs():
    print("in func 2")

def login():
    print("in func 3")


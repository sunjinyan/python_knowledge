import multiprocessing


def f(l,i):
    l.acquire()

    try:
        print("hello world",i)
    finally:
        l.release()


if __name__ == "__main__":

    #进程之间为什么需要锁？
    #虽然每个进程是独立的，但是他们共享同一个屏幕、键盘等。所以控制在stdout的时候是按部就班的一个一个打的
    lock = multiprocessing.Lock()

    for num in range(10):
        multiprocessing.Process(target=f,args=(lock,num)).start()
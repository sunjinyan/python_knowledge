import threading
import time


def run(n):
    semaphore.acquire() #信号量
    time.sleep(1)
    #   5个同时出结果  实际上是有一个完成就再进来一个新的
    print("run the thread : %s\n" % n)
    semaphore.release()


if  __name__ == "__main__":

    num = 0
    semaphore = threading.BoundedSemaphore(5)#信号量  最多允许5个线程同时运行  绑定信号量

    for i in  range(10):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.activeCount() != 1:
    pass
else:
    print("all threads done......")
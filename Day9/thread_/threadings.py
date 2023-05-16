import threading
import time


def run(n):
    # time.sleep(2)
    # print("task",n)
    lock.acquire()
    global num
    num += 1
    #释放锁
    lock.release()

#共享内存 获取锁
lock = threading.Lock()
# rlock = threading.RLock() 避免出现锁循环，使用递归锁
num = 0

t1  = threading.Thread(target=run,args=("t1",))  #有一个也要加逗号
t2  = threading.Thread(target=run,args=("t2",))  #有一个也要加逗号


t1.start()
t2.start()


print(num)
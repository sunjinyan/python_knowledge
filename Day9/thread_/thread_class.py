import threading
import time


class MyThread(threading.Thread):

    def __init__(self,n):
        super().__init__()
        # super(MyThread,self).__init__()
        self.n = n


    def  run(self) -> None: #必须叫run
        print("run in" , self.n,threading.currentThread(),threading.activeCount(),threading.active_count())
        time.sleep(0.1)
        print("task done")

tt1 = time.time()
t_objs  = []
#进程不会等子线程，就会继续往下执行
for i in range(25):
    t1 = MyThread("T1_"+str(i))
    t1.setDaemon(True)# 把当前线程设置成守护线程，必须在start之前设置
    t1.start() #调用run

    #不要在这里join
    # t1.join() #加了join就是线程的串行执行了，而不是并发执行
    t_objs.append(t1)#为了不阻塞后面的线程启动，不在这里join，先放到一个列表里

#有了setDaemon就 可以不用这个了
# for i in  t_objs:#这种方式就是并发执行了
#     i.join()#加了join就是线程的串行执行了，而不是并发执行 join的作用就是等待子线程执行结束


tt2 = time.time()

#主进程和守护进程，

#threading.active_count() 获取活跃线程数
#<_MainThread(MainThread, started 27040)> 打印主线程
print("taks done ",threading.currentThread(),threading.activeCount(),threading.active_count())
print(tt2 - tt1)



#python  同一时间执行的只有一个 所以就是单核单线程  由于GIL全局锁原因  是操作系统的原生线程




#线程锁

import multiprocessing
import time


#没有线程池，可以使用信号量模拟同时几个线程进行


#apply  apply_sync


def Foo(i):
    #子进程中 __name__是叫__mp_main__
    print(__name__,2)
    time.sleep(2)
    return  i + 100


def Bar(arg):
    print('-> exec done: ',arg)

#主进程中 __name__是叫__main__
#当被当作一个模块导入的时候 则__name__会叫模块名字了
print(__name__,1)
if __name__ == '__main__':

    # windows 可以加个这个  区分主动执行这个脚本还是从其他地方当一个模块调用 如果是从别的代码里导入，就不执行
    multiprocessing.freeze_support()

    #process 允许进程池里 同时放入 5个进程，去交给CPU处理，下边是处理了10个进程，
    #但同时运行的只有进程池中的5个，进程池中完成一个，再进一个，其他的进程是挂起状态
    pool = multiprocessing.Pool(processes=5)

    for i in range(10):
        # pool.apply_async(func=Foo,args=(i,),callback=Bar)  #异步执行 并行  callback回调执行完func之后再执行
        pool.apply(func=Foo,args=(i,)) #同步执行  串行

    print('end')

    #要先close  后 join  记住
    pool.close()
    pool.join()#进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭
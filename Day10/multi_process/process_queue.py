

#进程间通信的工具

'''
queue.Queue()是线程的q  出了进程就访问不到了

那么进程间也有进程间的Queue

'''
import multiprocessing
import queue
import threading


def f(q):
    q.put([42,None,'hello'])

# def ft():
#     qt.put([55,None,'hello '])  #这里的qt变量是全局的  父进程的qt 而不是局部的

if __name__ == '__main__':

    # qt = queue.Queue()
    # pt = threading.Thread(target=ft) #在子线程是可以直接不用传参直接访问父线程的 queue 但是进程不行
    #
    # pt.start()
    # print(qt.get())
    # pt.join()


    #但是进程不行  就算把qt当作 q传给子进程也会报错
    #会报错pickle _thread.lock


    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=f,args=(q,)) #相当于克隆了一份 给了子进程，子进程放了一份数据到克隆的里，有个中间部分序列化
    #pickle  然后又反序列化  传回父进程的进程队列中  因为没有中间放那么进程间无法共享
    p.start()

    print(q.get())#[42, None, 'hello']

    p.join()
import multiprocessing
import os


#进程间使用 manager 进行数据共享

def  f(d,l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None

    l.append(os.getpid())
    print(l)

if __name__ == '__main__':
    with multiprocessing.Manager() as manager: # manager =  multiprocessing.Manager()
        d = manager.dict() #生成一个字典 可以在多个进程间共享和传递

        l = manager.list(range(5)) #生成一个列表 可以在多个进程间共享和传递

        p_list = []

        for i in  range(10):
            p = multiprocessing.Process(target=f,args=(d,l))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)
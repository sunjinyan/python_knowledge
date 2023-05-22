import multiprocessing
import os


def info(title):
    print(title)
    print("module name: ",__name__)
    print('parent process: ',os.getppid())
    print('process id: ',os.getpid())
    print("\r\n")

def f(name):
    info('\033[31;1m function f \033[0m')
    print('hello',name)

if __name__ == '__main__':
    info('\033[32;1m main process line \033[0m')

    p = multiprocessing.Process(target=f,args=('bob',))
    p.start()
    p.join()
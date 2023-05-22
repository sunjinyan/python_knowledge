import multiprocessing
import threading
import time

# mul_pro = multiprocessing.Pool()

def thread_run():
    print(threading.get_ident())


def run(name):
    time.sleep(2)
    print('hello',name)
    t = threading.Thread(target=thread_run)
    t.start()

if __name__ == "__main__":
    for i in range(10):
        p = multiprocessing.Process(target=run,args=('bob {_id}'.format(_id=i),))
        p.start()
        # p.join()
import multiprocessing


def f(conn):
    print(conn.recv())
    conn.send([55,None,'hello'])
    conn.close()

if __name__ == "__main__":
    parent_conn,child_conn= multiprocessing.Pipe() #管道生成就会有两头，分别给两个进程
    parent_conn.send([11, None, 'hello  66'])
    p = multiprocessing.Process(target=f,args=(child_conn,))

    p.start()

    print(parent_conn.recv())
    p.join()
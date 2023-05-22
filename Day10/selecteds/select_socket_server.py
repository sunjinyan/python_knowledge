import queue

import select
import socket

server = socket.socket()



server.bind(('localhost',9999))


server.listen(1000)

#设置成非阻塞
server.setblocking(False)  #accept也不阻塞

msg_dic = {}

inputs = [server,]#想让内核检测的链接都在这里  给select检测这个服务的所有链接
# inputs = [server,conn1,conn2]#想让内核检测的链接都在这里  给select检测这个服务的所有链接

outputs = []#
# outputs = [r1，r2]#

while True:
    # xlist  #断了的链接都放到这里 也是inputs
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)
    # exceptional 异常链接 新来的链接都放这里readable   writeable

    # outputs 往outputs 放什么 下次就出来啥


    for r in readable:
        if r is server: # 代表来了一个新链接
            conn,addr = server.accept() #接受了一个新连接
            #如果使用了select 来检测链接，那么就该把这个放到inputs里去继续检测
            '''Traceback (most recent call last):
          File "D:\Learn\python_knowledge\Day10\selecteds\select_socket_server.py", line 28, in <module>
            print("recv:",conn.recv(1024))
        BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。
        否则会报错
        '''
            inputs.append(conn)
            # print(conn,addr)
            # print("recv:",conn.recv(1024))  因为这个这个新建立的链接还没发数据过来，现在就接受的话程序就报错了，所以要想实现这个客户端发数据来时
            #server端能知道，就需要让select再检测这个conn的链接，就append到inputs中就可以了
            msg_dic[conn] = queue.Queue()
        else:
            #是之前的conn 在这里直接收取数据就可以了
            # data = conn.recv(1024)
            data = r.recv(1024)
            print("recv:",data)
            msg_dic[r].put(data)

            outputs.append(r)#放入返回的链接队列中
            # r.send(data)
            # print("send down")

    for w in writeable:#要返回给客户端的链接列表

        data_to_client = msg_dic[w].get()
        w.send(data_to_client) #返回给客户端

        outputs.remove(w) #确保下次循环的时候 writeable不在返回旧链接了

    for e in exceptional:
        #如果出错，就把链接实例从 input  output中做下判断，存在就删除，肯定再input里边，

        inputs.remove(e)

        if e in     outputs:
            outputs.remove(e)

        del msg_dic[e]

import selectors
import socket

sel = selectors.DefaultSelector() #默认用epoll  win 没有的就使用selector


def accept(sock, mask): #sock是fileobj 文件句柄 相当于select还没建立链接的r
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read) #相当于自己亲手些的select 的放入队列的链接    并注册了回调函数为read
    #新连接再活动就调用的是read回调函数了


def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn) #socket没有数据 就在这里close  并关闭select的信息
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 9999))
sock.listen(100)
sock.setblocking(False)  #设置为非阻塞，如果想要使用select  就要使用非阻塞模式，false的时候就算accept都不再阻塞
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select() #默认就是阻塞，有活动链接就返回活动的链接列表
    for key, mask in events:

        callback = key.data #相当于   accept
        callback(key.fileobj, mask) #key.fileobj 就是socket的实例 相当于 conn，  mask
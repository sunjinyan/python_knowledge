import socket

srv = socket.socket()

srv.bind(('localhost',6969))

srv.listen(102)

while True:
    conn,addr = srv.accept() #等待 电话进来
    print(conn,addr)

    while True:
        # 不能直接调用 srv的recv  因为需要使用一个电话多个 接听的例子来分析
        re = conn.recv(1024) #有限制
        print(re.decode('utf-8'))
        if not re:
            print("client is closed")
        break
        conn.send(re.upper()) #有限制
        # conn.sendall(re.upper()) #循环发send
        if re.decode('utf-8') == "finish" or re.decode('utf-8') == "":
            break


srv.close()

import hashlib
import os.path
import socket

srv = socket.socket()


srv.bind(("localhost",9000))

srv.listen()

while True:
    conn,addr = srv.accept()

    while True:
        print("等待新的指令")
        data = conn.recv(1024)

        if not data:
            print("客户端已断开")
            break

        cmd,filename = data.decode().split()
        print("file  name ",filename)

        # if not os.path.isfile(filename) :
        if  os.path.isfile(filename) :
            f = open(filename,'rb')

            m = hashlib.md5()


            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode()) #send file size
            conn.recv(100) #wait for ack

            #send data
            for line in  f:
                m.update(line)
                conn.send(line)
            f.close()

            # 避免粘包 发送一个告知服务端
            #done  = conn.recv(1024)
            #print('client  done : ',done.decode())

            #最后双方进行md5校验验证
            print('file md5',m.hexdigest())
            conn.send(m.hexdigest().encode())
        print("send done")
srv.close()
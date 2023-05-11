import hashlib
import socket
import time

cli = socket.socket()


cli.connect(("localhost",9000))


while True:
    cmd = input(">>>: ")
    if cmd == "exit":
        break

    if len(cmd) == 0: continue

    cmd = cmd.strip()

    if cmd.startswith("get"):
        cli.send(cmd.encode())
        filesize = cli.recv(100) #接收数据大小
        print("文件大小: ",filesize)
        cli.send(b"ready please send")

        file_total_size = int(filesize.decode())

        filename = str(time.time()) + "_"  + cmd.split()[1]
        recieve_size = 0
        f = open(filename,'wb')

        m = hashlib.md5()
        while recieve_size < file_total_size: #黏在一块 就可能出现粘包现象，所以最好是接收和发送的文件大小相等

            if file_total_size - recieve_size > 1024: #表示要收不只是一次
                size = 1024
            else: #这样就不会粘包了 可以不适用ack  和 相应的处理
                size = file_total_size - recieve_size

            data = cli.recv(size)
            recieve_size += len(data)
            m.update(data)
            f.write(data)
            print(file_total_size,recieve_size)
        else:


            #避免粘包 发送一个告知服务端
            #cli.send(b'recv file  info done')

            new_file_md5 = m.hexdigest()
            print("file recv done ",recieve_size,file_total_size)
            f.flush()
            f.close()
        server_file_md5 = cli.recv(1024)
        print("server_file_md5",server_file_md5.decode())
        print("new_file_md5",new_file_md5)

cli.close()
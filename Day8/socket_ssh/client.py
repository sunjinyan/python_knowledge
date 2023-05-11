import socket

client = socket.socket()

client.connect(("localhost",9999))


try:
    while True:

        cmd = input(">>>:").strip()
        if len(cmd) <= 0: continue

        client.send(cmd.encode())

        rec_size = client.recv(100) #接收命令结果长度


        if not rec_size.decode("utf-8").isdigit() : continue

        print("cmd size : ",rec_size.decode("utf-8"))
        client.send(b'ready')#如果发看字需要使用encode，如果是字母数字的字符，直接加个b就可以 此处是回应服务器响应ack，解决粘包问题

        # receive_size  和  rec_size不相等的是引文decode后是 汉字占3个字节
        receive_size = 0
        receive_data = b''
        while receive_size < int(rec_size.decode("utf-8")): #不相等就一直收  循环收，直到每个命令的结果都返回
            data = client.recv(1024)
            receive_size +=      len(data) #每次收到的可能小于1024

            receive_data += data

            print(data.decode("utf-8"))
        else:
            print("cmd res receive done size %s" % str(receive_size))

except Exception as e:
    print(e)
    client.close()
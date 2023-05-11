import socket

cli = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0) #相当于 生成socket类型 并生成链接对象


cli.connect(("localhost",6969))

#pytion 只能发送 byte
# cli.send("Hello World" .encode("utf-8"))
# cli.send("测啊是".encode('utf-8'))正确
# cli.send(b"测啊是") 错误

# cli.send(b"Hello World")
cli.send("测啊a是".encode('utf-8'))

while True:

    data = cli.recv(1024)
    if not data:
        print("client is closed")
        break

    print("receive data %s \n" % data.decode('utf-8'))
    if data.decode('utf-8') == 'finish' or data.decode('utf-8') == 'FINISH' or data.decode('utf-8') == "":
        break

    msg = input("请输入消息>>>: ").strip()
    cli.send(msg.encode('utf-8'))

cli.close()
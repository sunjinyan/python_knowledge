import os
import socket
import time

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
server.bind(("localhost",9999))

server.listen()
error = False
while True:
    conn,addr = server.accept()
    print(conn,addr)

    while True:
        print("等待新的指令")
        data = conn.recv(1024)

        if not  data:
            print("客户端已断开")
            break

        cmd_res = ""
        try:

            print("执行指令")
            cmd_res = os.popen(data.decode()).read()

            #把执行完命令之后的长度首先计算下，然后告知客户端接下来要接收多少的长度命令
            cmd_len = len(cmd_res.encode('utf-8'))
            if  cmd_len == 0:
                cmd_res = "cmd has no output..."

            #先发大小给客户端
            conn.send(str(cmd_len).encode("utf-8"))

            #如果大于1024 该怎么处理？
            #缓冲区满了会发给客户端，超时也会
            #如果 两条消息紧接着发送 会出现在 接收端有 100Adddq...的粘包错误 就是说socket粘包
            #原因就是紧挨着 的两个send 会被缓冲区当作一条发送


            #可以使用sleep 凑合解决
            # time.sleep(0.5)

            client_ack = conn.recv(1024) #等待客户端返回相应  解决粘包问题

            conn.send(cmd_res.encode("utf-8"))#手动send  是强制超时的一种

        except Exception as e:
            error = True
            print("catch error %s" % e)
            cmd_res = "cmd has no output..."
            #conn.send(cmd_res.encode("utf-8"))
            break
    if  error:
        break

server.close()

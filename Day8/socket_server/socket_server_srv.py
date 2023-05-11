import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):


    #和客户端的交互都在这里处理的
    def handle(self) -> None: # 只做一次，如果想重复交互，就在handle里进行循环

        while True:

            try:
                self.data = self.request.recv(1024).strip()

                # print("{} wrote:".format(
                #     self.client_address[0]
                # ))
                # print("{0} wrote:".format(
                #     self.client_address[0]
                # ))
                print("{__address} wrote:".format(
                    __address=self.client_address[0]
                ))


                #在socket  server中不在想传统 socket中的一样判断发送的是空来判断客户端断开 ，而是使用异常 ConnectionResetError
                # if  not self.data:  #代表客户端断了
                #     print("client close")
                #     break
                print(self.data)
                self.request.sendall(self.data.upper())  #sendall就是重复调用send
            except ConnectionResetError as e:
                print("error ", e)
                break


if __name__ == "__main__":
    HOST,PORT = "0.0.0.0",9999

    # server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    # server = socketserver.ForkingTCPServer((HOST,PORT),MyTCPHandler)

    server.serve_forever()
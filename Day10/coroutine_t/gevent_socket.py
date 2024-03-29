

import sys
import socket
import time
import gevent

from gevent import socket,monkey


monkey.patch_all()

def server(port):
    s = socket.socket()

    s.bind(('0.0.0.0',port))

    s.listen(500)
    while True:
        cli,addr = s.accept()
        gevent.spawn(handel_request,cli)

def handel_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv:",data)
            conn.send(data)
            if not  data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as e:
        print(e)
    finally:

        conn.close()

if __name__ == "__main__":
    server(8001)
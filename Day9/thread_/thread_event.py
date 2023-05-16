

#

#
#
#
# 实现红绿灯的逻辑

'''
红绿灯的线程

和

车的线程

一个线程根据另一个线程的事件来决定

an event is a simple synchronization  object
事件就是用来做线程同步的

import threading

event = threading.Event()

event.set()
event.clear()

event.wait()#等着它设定

'''
import threading
import time

evt = threading.Event()
def lighter():
    count = 0
    evt.set() #先设置为绿灯
    while True:
        if count > 5 and count < 10: #改成红灯
            evt.clear() #把标志位清理
            print("\033[41;1mred light is on ... \033[0m")


        elif count > 10:
            evt.set() #变绿灯
            count = 0



        else:
            print("\033[42;1mgreen light is on ... \033[0m")

        time.sleep(1)
        count += 1

def car(name):
    while True:
        if evt.is_set() : #判断如果设置了标志位 _flag
            print("【%s】 running ..."%name)
            time.sleep(1)
        else:
            print("【%s】 wait ..."%name)
            evt.wait()

light  = threading.Thread(target=lighter)

light.start()

car1 = threading.Thread(target=car,args=("car1",))
car1.start()
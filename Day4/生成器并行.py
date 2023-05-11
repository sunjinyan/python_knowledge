import time


def consumer(name):
    print("%s 准备吃包子啦！" % name)
    while True:
        baozi = yield  #yield有产出的意思 保存当前状态并返回的作用，不往下执行 如果第二次调用next 只是调用了yield并没有给yield传值
        # send会调用yield给yield传值

        print("包子【%s】来了，被【%s】吃了！" %(baozi,name))

# c = consumer("aaa")
# c.__next__()
# c.send("纯肉")
# c.__next__()

def producer(name):

    #函数变成生成器
    c = consumer("A")
    c2 = consumer("B")

    #必须先执行两个next
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子")
        c.send(i)
        c2.send(i)

producer("lll")
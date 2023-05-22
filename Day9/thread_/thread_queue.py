import queue

q = queue.Queue(1024) #正常的 先进先出

# lifo = queue.LifoQueue()# 后进先出  也就是先进后出的队列 last  in  first  out Queue

# priority  = queue.PriorityQueue() #存储数据时可设置优先级的队列
# priority.put(("aaa",10)) 元组后边的权重越大越先出
# priority.put(("vvv",5))
# priority.put(("ads",1))

# q.put_nowait()
# q.get() #阻塞式等待 可以设置timeout=1 阻塞超时时间
# q.get_nowait() #非阻塞式等待，报异常

# q.qsize() 判断队列大小

# q.full() 判断队列是否满了

# q.empty()Return True if the queue is empty, False otherwise 判断一个队列是否为空

#q.join() #Blocks until all items in the Queue have been gotten and processed  阻塞直到queue被消费完毕


q.task_done()

#不用yield 做生产者消费者了，使用线程和  queue
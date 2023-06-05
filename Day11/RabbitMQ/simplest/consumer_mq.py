# _*_coding:utf-8_*_
__author__ = 'Alex Li'

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='47.93.20.75',port=5672))
channel = connection.channel()

# 为什么在这里消费者又声明了一个队列？ ‒在消费者里已经做过同样的声明了.
# 如果我们确认这个queue已经声明过了. For example if send.py program
# 但确保没有这个queue 在这里再声明一次避免异常出错
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello',durable=True)  #持久化durable=True


def callback(ch, method, properties, body):
    print('->>>',ch,method,properties)
    print(" [x] Received %r" % body)
    # ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1) #处理完这条再发下一条
channel.basic_consume(on_message_callback=callback,
                      queue='hello',
                      auto_ack=True #自动确认  如果设置为false  则需要在回调函数中 # ch.basic_ack(delivery_tag=method.delivery_tag)
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
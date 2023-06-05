#!/usr/bin/env python
import pika



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='47.93.20.75',port=5672)
)  #建立socket

channel = connection.channel() #声明一个管道

# 声明queue
channel.queue_declare(queue='hello',durable=True)  #持久化durable=True

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello', #就是 queue名字
                      body='Hello World!'.encode(),
                      properties=pika.BasicProperties(
                        delivery_mode=2, #把消息持久化 2
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()
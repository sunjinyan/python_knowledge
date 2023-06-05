import pika
import sys

connection = pika.BlockingConnection( pika.ConnectionParameters(host='47.93.20.75',port=5672))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout') #fanout 纯广播

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message.encode())
print(" [x] Sent %r" % message)
connection.close()
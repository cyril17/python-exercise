# -*- coding: utf-8 -*-
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#建立一个socket
channel = connection.channel()    #建立一个管道

# 声明queue
#channel.queue_declare(queue='hello2')
channel.queue_declare(queue='hello5',durable=True)
#加了durable之后就是消息持久化了
#durable只是把队列持久化了，但队列里的消息没有持久化

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello5',# queue名字
                      body='Hello World!',
                      properties = pika.BasicProperties
                          (
                           delivery_mode=2,  # make message persistent,消息的持久化
                          )
                      ) #消息内容
print(" [x] Sent 'Hello World!'")

connection.close()

'''
 [x] Sent 'Hello World!'
'''
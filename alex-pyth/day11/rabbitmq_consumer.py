# -*- coding: utf-8 -*-

import pika,time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
#channel.queue_declare(queue='hello2')
#因为不确定是生产者还是消费者哪个先运行，所以在两边都需要声明,不然会出错
channel.queue_declare(queue='hello5',durable=True)
#加了durable之后就是消息持久化了
#durable只是把队列持久化了，但队列里的消息没有持久化

def callback(ch, method, properties, body):  #回调函数
    print('---->',ch,method,properties)
    time.sleep(30)
    print(" [x] Received %r" % body)
    #消息处理完毕之后可能在运行其他函数，为了防止服务端一直等待，用下面的给服务端手动确认下
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
#﻿消息公平分发

#开始消费消息
channel.basic_consume(
                      callback,   #如果收到消息，就调用callback函数来处理消息
                      queue='hello5',  #定义从哪个队列里面收消息
                      #no_ack=True   一般不加这个，为了让服务器不确认，不加这个的话，消费者会轮询，
                      # 即如果1个消费者没有处理完的数据终止之后（即客户端没有给服务端确认）会自动交给下一个消费者去处理，
                     )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()   #只要程序一 直开着，就会一直收消息

'''
[*] Waiting for messages. To exit press CTRL+C
----> <BlockingChannel impl=<Channel number=1 OPEN conn=<SelectConnection OPEN socket=('127.0.0.1', 49444)->('127.0.0.1', 5672) params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>>>这个是管道的内存对象地址  <Basic.Deliver(['consumer_tag=ctag1.d94635de7d7e4f24868856a220ccff58', 'delivery_tag=1', 'exchange=', 'redelivered=False', 'routing_key=hello'])>包含把消息发给谁还有一些其他信息 <BasicProperties>
 [x] Received b'Hello World!'
'''
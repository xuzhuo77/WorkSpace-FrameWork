import pika
import json

credentials = pika.PlainCredentials('xuzhuo', 'xuzhuo77!')  # mq用户名和密码
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(pika.ConnectionParameters(host = '129.211.61.116',port = 5672,virtual_host = '/'
                                                               ,credentials = credentials))
channel=connection.channel()
# 声明消息队列，消息将在这个队列传递，如不存在，则创建
channel.queue_declare(queue='TEST01')

channel.basic_publish(exchange='',
                      routing_key='TEST01',
                      body='Hello Wo12312rld!')
connection.close()
import pika

credentials = pika.PlainCredentials('xuzhuo', 'xuzhuo77!')
connection = pika.BlockingConnection(pika.ConnectionParameters(host = '129.211.61.116',port = 5672,virtual_host = '/',credentials = credentials))
channel = connection.channel()
# 申明消息队列，消息在这个队列传递，如果不存在，则创建队列
channel.queue_declare(queue = 'TEST01', durable = False)
# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(body.decode())

# 告诉rabbitmq，用callback来接收消息
channel.basic_consume('TEST01',callback)
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()
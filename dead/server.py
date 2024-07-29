import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare('main', 'direct')
channel.exchange_declare('dlx', 'fanout')

channel.queue_declare(queue="mainq", arguments={'x-dead-letter-exchange': 'dlx', 'x-message-ttl': 5000, 'x-max-length': 5})
channel.queue_bind('mainq', 'main', 'home')

channel.queue_declare('dlxq')
channel.queue_bind('dlxq', 'dlx')


def dead_callback(ch, method, properties, body):
    print("[x] Dead Letter :", body)


channel.basic_consume('dlxq', on_message_callback=dead_callback, auto_ack=True)

print("Start consuming...")
channel.start_consuming()

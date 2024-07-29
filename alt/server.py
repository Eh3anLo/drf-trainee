import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.exchange_declare(exchange="alt", exchange_type="fanout")
ch.exchange_declare('main', 'direct', arguments={'alternate-exchange': 'alt'})

ch.queue_declare(queue='mainq')
ch.queue_bind('mainq', 'main', 'home')

ch.queue_declare(queue='altq')
ch.queue_bind('altq', 'alt')


def alt_callback(ch, method, properties, body):
    print("[x] Alt :", body)


def main_callback(ch, method, properties, body):
    print("[x] Main : ", body)


ch.basic_consume(queue='altq' , on_message_callback=alt_callback, auto_ack=True)
ch.basic_consume(queue='mainq' , on_message_callback=main_callback, auto_ack=True)

print("Start Consuming...")
ch.start_consuming()

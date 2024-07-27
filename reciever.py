import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch = connection.channel()

ch.queue_declare(queue="one")

def callback(ch, method, properties, body):
    print(f"Received {body}")
    print(method)
    ch.basic_ack(delivery_tag=method.delivery_tag)

#ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue="one" , on_message_callback=callback)
print("waiting for message ...")
ch.start_consuming()


                                     
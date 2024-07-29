import pika
import uuid
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

reply_queue = ch.queue_declare(queue='' , exclusive=True)


def on_message_reply(ch,method,properties,body):
    print("Reply received request: " , body)


ch.basic_consume(queue=reply_queue.method.queue, on_message_callback=on_message_reply, auto_ack=True)

cor_id = str(uuid.uuid4())
ch.queue_declare(queue='request-server')
ch.basic_publish(exchange='', routing_key="request-server", body="hello world", properties=pika.BasicProperties(
    reply_to=reply_queue.method.queue,
    correlation_id=cor_id
))
print("[x] Sending a Request ...")
ch.start_consuming()

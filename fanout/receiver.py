import pika

credentials = pika.PlainCredentials("ehsan" , "ehsan")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange="logs" , exchange_type="fanout")
ch_queue = ch.queue_declare(queue='' , exclusive=True)

ch.queue_bind(queue=ch_queue.method.queue , exchange='logs')

def callback(ch , method,properties , body):
    print(f"Received  {body}")
ch.basic_consume(queue=ch_queue.method.queue , on_message_callback=callback , auto_ack=True)

print("Waiting for logs ...")
print(ch_queue.method.queue)
ch.start_consuming()



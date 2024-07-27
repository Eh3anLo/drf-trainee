import pika

credentials = pika.PlainCredentials("ehsan" , "ehsan")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='notif_logs' , exchange_type='topic')
ch_queue = ch.queue_declare(queue="warnings" , exclusive=True)
queue_name = ch_queue.method.queue

ch.queue_bind(queue=queue_name , exchange='notif_logs' , routing_key="*.warning")
print(queue_name)
print("Waiting for warning...")
def callback(ch , method , properties , body):
    print(body)

ch.basic_consume(queue=queue_name , on_message_callback=callback , auto_ack=True)
ch.start_consuming()
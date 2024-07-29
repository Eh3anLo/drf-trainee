import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.queue_declare(queue="request-server")


def on_message_send_reply(channel, method, properties, body):
    print(f"[x] Received Request : {properties.correlation_id}")
    # reply
    ch.basic_publish(exchange='' , routing_key=properties.reply_to , body=f'Reply to {properties.correlation_id}')


ch.basic_consume(queue="request-server" , on_message_callback=on_message_send_reply , auto_ack=True)

print("[*] Waiting for request ....")
ch.start_consuming()

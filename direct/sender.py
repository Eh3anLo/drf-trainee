import pika
import time

credentials = pika.PlainCredentials("ehsan" , "ehsan")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost" , credentials=credentials))
ch = connection.channel()
ch.queue_declare(queue="one")

ch.basic_publish(exchange="",
                 routing_key="one",
                 body="hello world",
                 properties=pika.BasicProperties(
                     content_type='text/plain',
                     type='exchange.queue',
                     headers={'name' : "say hello"},
                     content_encoding='gzip',
                     timestamp=int(time.time())
                 ))
print(" [x] Sent 'Hello World!'")

connection.close()
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.exchange_declare(exchange="alt", exchange_type="fanout")
ch.exchange_declare('main', 'direct', arguments={'alternate-exchange': 'alt'})

ch.basic_publish('main', 'bad', 'Hello world')

print("Sent ...")
connection.close()



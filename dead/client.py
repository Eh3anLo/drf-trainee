import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="main", exchange_type='direct')
channel.basic_publish(exchange="main", routing_key='home', body="hello world")

print("Sent...")
connection.close()

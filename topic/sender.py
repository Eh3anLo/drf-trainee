import pika

credentials = pika.PlainCredentials("ehsan" , "ehsan")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange="notif_logs" , exchange_type="topic")

messages = {
    "notif.errors" : "This is error message",
    "notif.warning" : "This is warning message",
}

for key , value in messages.items():
    ch.basic_publish(exchange="notif_logs",routing_key=key , body=value)

print("Log sented ....")
connection.close()
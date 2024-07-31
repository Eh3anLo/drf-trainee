from celery import Celery, group

app = Celery('one', broker="amqp://guest:guest@localhost:5672", backend="rpc://")

@app.task()
def add(a, b):
    return a+b

@app.task()
def mines(a, b):
    return a-b

result = add.signature((5,6)).delay()

print(result.get())


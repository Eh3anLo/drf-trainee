from celery import Celery, group

app = Celery('two', broker="amqp://guest:guest@localhost:5672", backend="rpc://")

@app.task()
def add(a, b):
    return a+b

@app.task()
def mines(a, b):
    return a-b

result = group(add.s(1,2), mines.s(4,3))

print(result().get())

